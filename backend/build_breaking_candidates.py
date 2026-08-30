#!/usr/bin/env python3
"""Build a cross-channel candidate pool for the daily major developments desk."""

from __future__ import annotations

import argparse
import gzip
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from aix_pipeline import CHANNELS, natural_key
from daily_digest import load_json, write_json


OFFICIAL_ACCOUNTS = {
    "openai", "anthropicai", "googledeepmind", "metaai", "msftresearch",
    "nvidiaai", "huggingface", "mistralai", "xai", "cohere", "allen_ai",
}
MAJOR_TERMS = (
    "breakthrough", "solved", "proof", "conjecture", "counterexample", "first",
    "record", "discovery", "launch", "release", "open source", "new model",
    "重大", "突破", "证明", "猜想", "反例", "首次", "发布", "开源",
)


def read_x_cache(root: Path, run_date: date) -> list[dict[str, Any]]:
    path = root / "work" / "source-cache" / "x" / f"{run_date}.json.gz"
    if not path.exists():
        return []
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        value = __import__("json").load(stream)
    return value if isinstance(value, list) else []


def infer_channel(item: dict[str, Any]) -> str:
    text = f"{item.get('title', '')} {item.get('abstract_or_text', '')}".lower()
    if any(term in text for term in ("theorem", "proof", "conjecture", "geometry", "lean", "coq", "mathemat")):
        return "aixmath"
    if any(term in text for term in ("protein", "genom", "cell", "clinical", "biology", "biomedical")):
        return "aixbio"
    if any(term in text for term in ("chem", "molecule", "drug", "catal", "material", "crystal")):
        return "aixchem"
    if any(term in text for term in ("github", "repository", "framework", "sdk", "inference", "developer")):
        return "engineering"
    return str(item.get("channel") or "aivoices")


def source_status(item: dict[str, Any]) -> str:
    username = str((item.get("metadata") or {}).get("username") or "").lower()
    status = str(item.get("publication_status") or "")
    if username in OFFICIAL_ACCOUNTS or status in {"official_update", "release"}:
        return "official_announcement"
    if status in {"preprint", "peer_reviewed", "researcher_announcement"}:
        return status
    if item.get("source") == "X":
        return "public_post"
    return "reported_result"


def editorial_score(item: dict[str, Any], selected: bool) -> int:
    text = f"{item.get('title', '')} {item.get('abstract_or_text', '')}".lower()
    metrics = item.get("metrics") or {}
    engagement = sum(int(metrics.get(name) or 0) for name in ("like_count", "repost_count", "reply_count", "quote_count"))
    priority = int((item.get("metadata") or {}).get("editorial_priority") or 0)
    score = 45 + (16 if selected else 0) + min(24, sum(term in text for term in MAJOR_TERMS) * 4)
    score += min(12, int(engagement ** 0.5) // 8)
    return min(100, max(score, priority))


def build(root: Path, site_root: Path, run_date: date) -> dict[str, Any]:
    pool: list[dict[str, Any]] = []
    for channel in CHANNELS:
        payload = load_json(site_root / "data" / "channels" / channel / "latest.json", {})
        if str(payload.get("date") or "") != run_date.isoformat():
            continue
        for item in payload.get("items") or []:
            value = dict(item)
            value["channel"] = channel
            value["candidate_origin"] = "channel_selection"
            value["editorial_score"] = editorial_score(value, True)
            value["source_status"] = source_status(value)
            pool.append(value)

    for item in read_x_cache(root, run_date):
        value = dict(item)
        value["channel"] = infer_channel(value)
        value["candidate_origin"] = "social_signal"
        value["editorial_score"] = editorial_score(value, False)
        value["source_status"] = source_status(value)
        pool.append(value)

    signals = load_json(root / "config" / "editorial_signals.json", {}).get("items") or []
    for item in signals:
        published = date.fromisoformat(str(item.get("published_at"))[:10])
        active_until = date.fromisoformat(str(item.get("active_until") or item.get("published_at"))[:10])
        if published <= run_date <= active_until:
            value = dict(item)
            value["candidate_origin"] = "editorial_signal"
            value["editorial_score"] = editorial_score(value, False)
            value["source_status"] = source_status(value)
            pool.append(value)

    unique: dict[str, dict[str, Any]] = {}
    for item in pool:
        key = natural_key(item) or str(item.get("id") or "")
        if key and (key not in unique or int(item.get("editorial_score") or 0) > int(unique[key].get("editorial_score") or 0)):
            unique[key] = item
    items = sorted(unique.values(), key=lambda item: (int(item.get("editorial_score") or 0), str(item.get("published_at") or "")), reverse=True)[:120]
    payload = {
        "schema_version": "1.0",
        "date": run_date.isoformat(),
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "count": len(items),
        "items": items,
    }
    write_json(site_root / "data" / "breaking" / "candidates" / "latest.json", payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--site-root", type=Path, default=Path("public"))
    parser.add_argument("--date", required=True)
    args = parser.parse_args()
    payload = build(args.root.resolve(), args.site_root.resolve(), date.fromisoformat(args.date))
    print(f"Major developments candidates ready: {payload['date']}; count={payload['count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
