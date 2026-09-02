import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError


ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "backend"
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from aix_pipeline import (  # noqa: E402
    GitHubTrendingParser,
    Runtime,
    build_x_queries,
    collection_window,
    http_error_message,
    openreview_invitation,
    publication_date,
    within_window,
)
from daily_digest import ARXIV_CATEGORIES, arxiv_category_query, fetch_arxiv, load_json  # noqa: E402
from build_breaking_candidates import channel_payload, previous_breaking_keys  # noqa: E402
from backfill_breaking_news import apply as apply_breaking_backfill  # noqa: E402
from backfill_engineering_trending import parse_snapshot  # noqa: E402
from publish_daily import factual_overview  # noqa: E402


class SourceWindowTests(unittest.TestCase):
    def test_historical_breaking_builder_reads_dated_channel_archive(self):
        with tempfile.TemporaryDirectory() as directory:
            site_root = Path(directory)
            archive = site_root / "data" / "channels" / "aixchem" / "archive" / "2026-08-01.json"
            archive.parent.mkdir(parents=True)
            archive.write_text('{"date":"2026-08-01","items":[{"id":"paper:1"}]}', encoding="utf-8")
            value = channel_payload(site_root, "aixchem", date(2026, 8, 1))
            self.assertEqual(value["items"][0]["id"], "paper:1")

    def test_breaking_backfill_updates_dated_archives_without_changing_latest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site_root = root / "public"
            candidates_root = root / "candidates"
            candidates_root.mkdir(parents=True)
            (candidates_root / "2026-08-01.json").write_text(
                '{"items":[{"id":"x:1","channel":"aivoices","source":"X","url":"https://x.com/a/status/1"}]}',
                encoding="utf-8",
            )
            for relative in ("data/daily/archive/2026-08-01.json", "data/archive/2026-08-01.json"):
                path = site_root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('{"date":"2026-08-01","breaking_news":[]}', encoding="utf-8")
            curation = root / "curation.json"
            curation.write_text(
                '{"days":[{"date":"2026-08-01","editor_note":"每日精选",'
                '"selected":[{"id":"x:1","headline_zh":"标题","summary_zh":"摘要",'
                '"why_breaking_zh":"意义"}]}]}',
                encoding="utf-8",
            )
            days, items = apply_breaking_backfill(site_root, candidates_root, curation)
            self.assertEqual((days, items), (1, 1))
            self.assertFalse((site_root / "data" / "breaking" / "latest.json").exists())
            daily = load_json(site_root / "data" / "daily" / "archive" / "2026-08-01.json", {})
            self.assertEqual(daily["breaking_news"][0]["id"], "x:1")

    def test_historical_trending_parser_preserves_language_rank_and_date_identity(self):
        markdown = """## 2026-08-01
#### python
* [openai / codex](https://github.com/openai/codex):Coding agent
* [deepchem / deepchem](https://github.com/deepchem/deepchem):Scientific machine learning
"""
        items = parse_snapshot(markdown, date(2026, 8, 1))
        self.assertEqual([item["metadata"]["language_rank"] for item in items], [1, 2])
        self.assertEqual(items[0]["metadata"]["trending_id"], "2026-08-01:openai/codex")
        self.assertEqual(items[0]["source"], "GitHub Trending")

    def test_previous_breaking_news_is_excluded_by_id_and_url(self):
        with tempfile.TemporaryDirectory() as directory:
            site_root = Path(directory)
            archive = site_root / "data" / "breaking" / "archive"
            archive.mkdir(parents=True)
            (archive / "2026-08-30.json").write_text(
                '{"items":[{"id":"x:42","url":"https://x.com/example/status/42?ref=home"}]}',
                encoding="utf-8",
            )
            keys = previous_breaking_keys(site_root, date(2026, 8, 31))
            self.assertIn("id:x:42", keys)
            self.assertIn("url:https://x.com/example/status/42", keys)

    def test_github_trending_parser_keeps_ranked_repository_metadata(self):
        parser = GitHubTrendingParser()
        parser.feed(
            '<article class="Box-row"><h2><a href="/openai/codex">Codex</a></h2>'
            '<p class="col-9">Coding agent</p><span itemprop="programmingLanguage">Rust</span>'
            '<span class="float-sm-right">1,234 stars today</span></article>'
        )
        self.assertEqual(parser.items[0]["repository"], "openai/codex")
        self.assertEqual(parser.items[0]["description"], "Coding agent")
        self.assertEqual(parser.items[0]["language"], "Rust")
        self.assertEqual(parser.items[0]["stars_today"], 1234)

    def test_github_utc_evening_counts_as_shanghai_next_day(self):
        self.assertEqual(publication_date("2026-08-16T20:00:00Z"), date(2026, 8, 17))
        self.assertTrue(within_window("2026-08-16T20:00:00Z", date(2026, 8, 17), date(2026, 8, 17)))
        self.assertFalse(within_window("2026-08-16T07:24:37Z", date(2026, 8, 17), date(2026, 8, 17)))
        self.assertTrue(within_window("2026-08-16T07:24:37Z", date(2026, 8, 15), date(2026, 8, 17)))

    def test_monday_window_includes_friday_arxiv(self):
        start, end = collection_window(date(2026, 8, 17))
        self.assertEqual(end, date(2026, 8, 17))
        self.assertLessEqual(start, date(2026, 8, 14))
        start_tue, _ = collection_window(date(2026, 8, 18))
        self.assertEqual(start_tue, date(2026, 8, 15))

    def test_arxiv_query_uses_categories_not_submitted_date_only(self):
        query = arxiv_category_query(ARXIV_CATEGORIES)
        self.assertIn("cat:cs.LG", query)
        self.assertIn("cat:cs.LO", query)
        self.assertIn("cat:math.LO", query)
        self.assertNotIn("submittedDate", query)

    def test_openreview_invitation_defaults(self):
        self.assertEqual(openreview_invitation("TMLR"), "TMLR/-/Submission")
        self.assertEqual(openreview_invitation("ICLR.cc/2026/Conference"), "ICLR.cc/2026/Conference/-/Submission")
        self.assertEqual(openreview_invitation("TMLR/-/Submission"), "TMLR/-/Submission")

    def test_x_queries_are_batched_for_grok(self):
        watchlists = {
            "x_accounts": [f"user{i}" for i in range(34)],
            "x_topic_queries": ["one", "two", "three", "four"],
        }
        queries = build_x_queries(watchlists, date(2026, 8, 16), date(2026, 8, 19))
        kinds = [kind for kind, _ in queries]
        self.assertEqual(kinds.count("topics"), 4)
        self.assertGreaterEqual(kinds.count("accounts"), 6)
        self.assertIn("from:user0", queries[0][1])
        self.assertIn("since:2026-08-16", queries[0][1])
        self.assertIn("until:2026-08-20", queries[0][1])
        self.assertNotIn("api.x.com", queries[0][1])

    def test_http_error_messages_are_explicit(self):
        self.assertIn("额度不足", http_error_message(HTTPError("https://example.com", 402, "Payment Required", hdrs=None, fp=None)))
        self.assertIn("请求过于频繁", http_error_message(HTTPError("https://example.com", 429, "Too Many Requests", hdrs=None, fp=None)))
        self.assertNotIn("Developer Console", http_error_message(HTTPError("https://example.com", 402, "Payment Required", hdrs=None, fp=None)))

    def test_overview_leads_with_real_counts(self):
        channels = [
            {"name": "AI × Chem", "stats": {"selected": 16}},
            {"name": "AI × Bio", "stats": {"selected": 10}},
            {"name": "AI × Math", "stats": {"selected": 0}},
        ]
        text = factual_overview(channels, "今日AI×化学与AI×生物各有16项精选。")
        self.assertTrue(text.startswith("今日精选：AI × Chem 16 项，AI × Bio 10 项，AI × Math 0 项。"))


class PipelineContractTests(unittest.TestCase):
    def test_runner_injects_github_token_and_skips_empty_cache(self):
        runner = (ROOT / "ops" / "run_local_pipeline.ps1").read_text(encoding="utf-8")
        pipeline = (ROOT / "backend" / "aix_pipeline.py").read_text(encoding="utf-8")
        self.assertIn("gh auth token", runner)
        self.assertIn("GITHUB_TOKEN", runner)
        self.assertIn("function Invoke-Python", runner)
        self.assertIn("Write-Host $line", runner)
        self.assertIn("Retry complete; still failed", runner)
        self.assertIn("All channels failed after retry; skip combined publish", runner)
        self.assertIn("$DiffCode -eq 1", runner)
        self.assertIn("git diff failed with exit code", runner)
        self.assertIn("if not values:", pipeline)
        self.assertIn("within_window(published, start, end)", pipeline)
        self.assertIn("x_harvest_protocol.md", runner)
        self.assertIn("function Invoke-GrokVisit", runner)
        self.assertIn("grok.exe", runner)
        self.assertIn("daily_visit_prompt.md", runner)
        self.assertTrue((ROOT / "ops" / "grok" / "daily_visit_prompt.md").exists())
        visit_prompt = (ROOT / "ops" / "grok" / "daily_visit_prompt.md").read_text(encoding="utf-8")
        self.assertIn("日期最新且 `ready=false`", visit_prompt)
        self.assertIn("已经 `ready=true` 的票不再检索", visit_prompt)
        self.assertTrue((ROOT / "AGENTS.md").exists())
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Codex 不执行 `ops/grok/daily_visit_prompt.md`", agents)
        self.assertIn("仅当当前执行者是 Grok", agents)
        self.assertNotIn("XBearerToken", runner)
        self.assertNotIn("X_BEARER_TOKEN", runner)
        self.assertNotIn("X_BEARER_TOKEN", pipeline)
        self.assertNotIn("api.x.com", pipeline)
        self.assertIn("arXiv API returned no entries", (ROOT / "backend" / "daily_digest.py").read_text(encoding="utf-8"))
        self.assertIn("当日未更新，未纳入本期", (ROOT / "backend" / "publish_daily.py").read_text(encoding="utf-8"))
        self.assertNotIn('published[:10] != runtime.run_date.isoformat()', pipeline)
        self.assertNotIn('submittedDate:[', (ROOT / "backend" / "daily_digest.py").read_text(encoding="utf-8"))

    def test_broken_research_feeds_are_removed(self):
        watchlists = (ROOT / "config" / "watchlists.json").read_text(encoding="utf-8")
        self.assertNotIn("www.anthropic.com/news/rss.xml", watchlists)
        self.assertNotIn("allenai.org/blog/rss.xml", watchlists)
        self.assertIn("importai.substack.com/feed", watchlists)


class EmptyArxivAndSuccessTests(unittest.TestCase):
    def test_empty_arxiv_first_page_is_an_error(self):
        empty = b'<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom"></feed>'
        with patch("daily_digest.http_get", return_value=empty):
            with self.assertRaisesRegex(RuntimeError, "no entries"):
                fetch_arxiv(date(2026, 8, 18), date(2026, 8, 18))

    def test_old_arxiv_entries_are_an_empty_window_not_success_page(self):
        atom = (
            b'<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom">'
            b"<entry><id>http://arxiv.org/abs/2301.00001</id><title>Old</title>"
            b"<summary>Abstract</summary><published>2020-01-01T00:00:00Z</published>"
            b"<updated>2020-01-01T00:00:00Z</updated><author><name>Ada</name></author>"
            b'<category term="cs.LG"/></entry></feed>'
        )
        with patch("daily_digest.http_get", return_value=atom):
            self.assertEqual(fetch_arxiv(date(2026, 8, 18), date(2026, 8, 18)), [])

    def test_mark_success_does_not_advance_on_empty_count(self):
        with tempfile.TemporaryDirectory() as directory:
            runtime = Runtime(Path(directory), date(2026, 8, 18))
            runtime.mark_success("arxiv", 0)
            self.assertEqual(load_json(runtime.state_path, {}), {})
            runtime.mark_success("arxiv", 3)
            self.assertIn("arxiv", load_json(runtime.state_path, {}))


if __name__ == "__main__":
    unittest.main()
