#!/usr/bin/env python3
"""Prepare and apply dated OpenReview additions for AI x Math archives.

This utility is deliberately scoped to OpenReview.  It never refreshes arXiv,
never creates Issues, and leaves existing Math selections in place.
"""

from __future__ import annotations

import argparse
import gzip
import json
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from aix_pipeline import (
    CHANNEL_META,
    LIMITS,
    SHANGHAI,
    THRESHOLDS,
    Runtime,
    fetch_openreview,
    previously_reported_keys,
    publication_date,
    report_key,
    score_item,
)
from daily_digest import (
    archive_index_entry,
    author_line,
    clean_text,
    load_json,
    looks_cjk,
    publish_tags,
    slim_public_item,
    write_json,
)


def dates_between(start: date, end: date) -> list[date]:
    return [start + timedelta(days=offset) for offset in range((end - start).days + 1)]


def channel_archive(site_root: Path, day: str) -> Path:
    return site_root / "data" / "channels" / "aixmath" / "archive" / f"{day}.json"


def existing_items(site_root: Path, day: str) -> list[dict[str, Any]]:
    return list(load_json(channel_archive(site_root, day), {}).get("items") or [])


def prepare(root: Path, site_root: Path, start: date, end: date, output_root: Path) -> None:
    watchlists = load_json(root / "config" / "watchlists.json", {})
    # One authenticated pass covers the requested month.  The regular collector
    # deliberately uses a short rolling window; replaying that window per day
    # would ask each OpenReview domain for the same records many times.
    runtime = Runtime(root, end)
    runtime.window = lambda _source: (start, end)  # type: ignore[method-assign]
    runtime.cache = lambda _name, build: build()  # type: ignore[method-assign]
    monthly = fetch_openreview(runtime, watchlists)
    by_day: dict[date, list[dict[str, Any]]] = {}
    for item in monthly:
        published = publication_date(item.get("published_at", ""))
        if published:
            by_day.setdefault(published, []).append(item)
    for run_date in dates_between(start, end):
        raw = by_day.get(run_date, [])
        cache_path = root / "work" / "source-cache" / "openreview" / f"{run_date}.json.gz"
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(cache_path, "wt", encoding="utf-8") as stream:
            json.dump(raw, stream, ensure_ascii=False, separators=(",", ":"))
        reported = previously_reported_keys(site_root, run_date)
        current = {report_key(item) for item in existing_items(site_root, str(run_date))}
        candidates = []
        suppressed = 0
        for item in raw:
            key = report_key(item)
            if key in reported or key in current:
                suppressed += 1
                continue
            score = score_item(item, "aixmath")
            if score >= max(45, THRESHOLDS["aixmath"] - 15):
                candidates.append(item)
        candidates.sort(key=lambda item: (-float(item.get("quality_score") or 0), item.get("title") or ""))
        prior = existing_items(site_root, str(run_date))
        payload = {
            "schema_version": "1.0",
            "date": str(run_date),
            "channel": "aixmath",
            "source": "OpenReview",
            "existing_selected": len(prior),
            "selection_capacity": max(0, LIMITS["aixmath"] - len(prior)),
            "fetched": len(raw),
            "suppressed_previous": suppressed,
            "count": len(candidates),
            "items": candidates[:60],
        }
        write_json(output_root / f"{run_date}.candidates.json", payload)
        print(f"{run_date}: fetched={len(raw)} candidates={len(candidates)} capacity={payload['selection_capacity']}")


def reviewed_item(item: dict[str, Any], review: dict[str, Any], rank: int) -> dict[str, Any]:
    summary = clean_text(review.get("summary_zh"))
    reason = clean_text(review.get("why_it_matters_zh"))
    abstract_zh = clean_text(review.get("abstract_zh"))
    source_abstract = clean_text(item.get("abstract_or_text") or item.get("abstract"))
    if looks_cjk(source_abstract) and not abstract_zh:
        abstract_zh = source_abstract
    if len(summary) < 20 or len(reason) < 16 or (source_abstract and not abstract_zh):
        raise ValueError(f"Review text is incomplete for {item['id']}")
    score = float(review.get("quality_score") or item.get("quality_score") or 0)
    if score < THRESHOLDS["aixmath"]:
        raise ValueError(f"Selected item score is below threshold: {item['id']}")
    output = dict(item)
    output.update({
        "summary_zh": summary,
        "why_it_matters_zh": reason,
        "abstract_zh": abstract_zh,
        "quality_score": min(100, score),
        "category": clean_text(review.get("category")) or item.get("category"),
        "tags": publish_tags(clean_text(review.get("category")) or item.get("category"), review.get("tags") or []),
        "evidence_flags": list(dict.fromkeys([clean_text(value) for value in review.get("evidence_flags", []) if clean_text(value)] + list(item.get("evidence_flags") or [])))[:6],
        "related_channels": [value for value in review.get("related_channels", item.get("related_channels", [])) if value and value != "aixmath"],
        "rank": rank,
        "featured": rank <= 3,
        "published": str(item.get("published_at") or "")[:10],
        "author_line": author_line(item.get("creators") or item.get("authors") or []),
    })
    return slim_public_item(output, include_abstract=True, clip_release=True)


def fresh_payload(day: str) -> dict[str, Any]:
    title, subtitle = CHANNEL_META["aixmath"]
    return {
        "schema_version": "2.0", "date": day, "channel": "aixmath",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "title": title, "subtitle": subtitle,
        "window": {"start": day, "end": day},
        "method": "OpenReview 公开元数据采集、历史去重、规则筛选与模型审阅",
        "method_note": "本期仅补充此前未展示的 OpenReview 公开投稿；内容依据公开摘要审阅。",
        "stats": {"fetched": 0, "suppressed_previous": 0, "candidates": 0, "selected": 0, "sources": {"OpenReview": 0}},
        "source_status": {"OpenReview": {"state": "empty", "count": 0}},
        "source_errors": [], "items": [],
    }


def update_index(site_root: Path, payload: dict[str, Any]) -> None:
    root = site_root / "data" / "channels" / "aixmath" / "archive"
    index_path = root / "index.json"
    index = load_json(index_path, {"schema_version": "2.0", "items": []})
    records = [item for item in index.get("items", []) if item.get("date") != payload["date"]]
    stats = payload.get("stats") or {}
    records.append(archive_index_entry(payload["date"], selected=stats.get("selected", 0), candidates=stats.get("candidates", 0), fetched=stats.get("fetched", 0), href=f"data/channels/aixmath/archive/{payload['date']}.json"))
    index["schema_version"] = "2.0"
    index["items"] = sorted(records, key=lambda item: item["date"], reverse=True)
    write_json(index_path, index)


def update_combined_archive(site_root: Path, payload: dict[str, Any]) -> None:
    for path in [site_root / "data" / "daily" / "archive" / f"{payload['date']}.json", site_root / "data" / "daily" / "latest.json"]:
        daily = load_json(path, {})
        if daily.get("date") != payload["date"]:
            continue
        for channel in daily.get("channels") or []:
            if channel.get("id") != "aixmath":
                continue
            channel["stats"] = dict(payload.get("stats") or {})
            channel["source_errors"] = list(payload.get("source_errors") or [])
            channel["items"] = [slim_public_item(item, include_abstract=path.name != "latest.json", clip_release=True) for item in payload.get("items") or []]
        write_json(path, daily)
        if path.parent.name == "archive":
            index_path = path.parent / "index.json"
            index = load_json(index_path, {"schema_version": "2.0", "items": []})
            selected = sum(int(channel.get("stats", {}).get("selected") or 0) for channel in daily.get("channels") or [])
            for entry in index.get("items") or []:
                if entry.get("date") == payload["date"]:
                    entry["selected"] = selected
            write_json(index_path, index)


def apply(site_root: Path, candidate_root: Path, curation_root: Path, start: date, end: date) -> None:
    for run_date in dates_between(start, end):
        day = str(run_date)
        candidate = load_json(candidate_root / f"{day}.candidates.json", {})
        curation = load_json(curation_root / f"{day}.json", {})
        reviewed = bool(curation)
        if not candidate:
            continue
        if not curation and (int(candidate.get("count") or 0) == 0 or int(candidate.get("selection_capacity") or 0) == 0):
            curation = {"date": day, "channel": "aixmath", "editor_note": "OpenReview 已完成查询，今日无新增可审阅条目。", "selected": []}
        if not curation:
            raise ValueError(f"Missing curation for {day}")
        if curation.get("date") != day or curation.get("channel") != "aixmath":
            raise ValueError(f"Curation metadata mismatch for {day}")
        existing = load_json(channel_archive(site_root, day), fresh_payload(day))
        items = list(existing.get("items") or [])
        by_id = {item["id"]: item for item in candidate.get("items") or []}
        seen = {report_key(item) for item in items}
        selected = curation.get("selected") or []
        capacity = int(candidate.get("selection_capacity") or 0)
        if len(selected) > capacity:
            raise ValueError(f"Curation exceeds remaining capacity for {day}")
        additions = []
        for review in selected:
            item = by_id.get(str(review.get("id") or ""))
            if not item:
                raise ValueError(f"Unknown curation item for {day}")
            key = report_key(item)
            if key in seen:
                raise ValueError(f"Duplicate report identity for {day}")
            seen.add(key)
            additions.append(reviewed_item(item, review, len(items) + len(additions) + 1))
        items.extend(additions)
        stats = dict(existing.get("stats") or {})
        stats["fetched"] = int(stats.get("fetched") or 0) + int(candidate.get("fetched") or 0)
        stats["candidates"] = int(stats.get("candidates") or 0) + int(candidate.get("count") or 0)
        stats["suppressed_previous"] = int(stats.get("suppressed_previous") or 0) + int(candidate.get("suppressed_previous") or 0)
        stats["selected"] = len(items)
        sources = dict(stats.get("sources") or {})
        sources["OpenReview"] = int(sources.get("OpenReview") or 0) + int(candidate.get("fetched") or 0)
        stats["sources"] = sources
        existing["items"] = items
        existing["stats"] = stats
        existing["generated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        existing["source_status"] = dict(existing.get("source_status") or {})
        existing["source_status"]["OpenReview"] = {"state": "ok" if candidate.get("fetched") else "empty", "count": int(candidate.get("fetched") or 0)}
        existing["source_errors"] = [
            message for message in existing.get("source_errors") or []
            if not str(message).startswith("OpenReview:")
        ]
        if reviewed:
            existing["review"] = {"model": "gpt-5.6-terra", "reasoning_effort": "high", "note": clean_text(curation.get("editor_note"))}
        write_json(channel_archive(site_root, day), existing)
        update_index(site_root, existing)
        update_combined_archive(site_root, existing)
        print(f"{day}: added={len(additions)} total={len(items)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("prepare", "apply"))
    parser.add_argument("--start", required=True, type=date.fromisoformat)
    parser.add_argument("--end", required=True, type=date.fromisoformat)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--site-root", type=Path, default=Path("public"))
    parser.add_argument("--candidate-root", type=Path, default=Path("work/openreview-math-backfill/candidates"))
    parser.add_argument("--curation-root", type=Path, default=Path("work/openreview-math-backfill/curations"))
    args = parser.parse_args()
    if args.end < args.start:
        raise ValueError("end date is before start date")
    if args.command == "prepare":
        prepare(args.root.resolve(), args.site_root.resolve(), args.start, args.end, args.candidate_root.resolve())
    else:
        apply(args.site_root.resolve(), args.candidate_root.resolve(), args.curation_root.resolve(), args.start, args.end)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
