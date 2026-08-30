#!/usr/bin/env python3
"""Resolve the major developments editor output against the candidate pool."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from daily_digest import load_json, write_json


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("curation", type=Path)
    parser.add_argument("--site-root", type=Path, default=Path("public"))
    args = parser.parse_args()
    candidates = load_json(args.site_root / "data" / "breaking" / "candidates" / "latest.json", {})
    curation = load_json(args.curation, {})
    if curation.get("date") != candidates.get("date"):
        raise RuntimeError("Major developments date does not match the candidate pool")
    by_id = {str(item.get("id")): item for item in candidates.get("items") or []}
    items = []
    seen = set()
    for rank, selected in enumerate((curation.get("selected") or [])[:3], 1):
        item_id = str(selected.get("id") or "")
        if item_id in seen or item_id not in by_id:
            continue
        seen.add(item_id)
        source = by_id[item_id]
        items.append({
            "id": item_id,
            "rank": rank,
            "channel": str(source.get("channel") or "aivoices"),
            "source": str(source.get("source") or ""),
            "source_status": str(source.get("source_status") or "reported_result"),
            "item_type": str(source.get("item_type") or "update"),
            "headline_zh": str(selected.get("headline_zh") or source.get("title") or ""),
            "summary_zh": str(selected.get("summary_zh") or source.get("summary_zh") or ""),
            "why_breaking_zh": str(selected.get("why_breaking_zh") or ""),
            "url": str(source.get("url") or ""),
            "published_at": str(source.get("published_at") or ""),
            "creators": source.get("creators") or [],
            "metrics": source.get("metrics") or {},
            "metadata": source.get("metadata") or {},
        })
    payload = {
        "schema_version": "1.0",
        "date": candidates.get("date"),
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "editor_note": str(curation.get("editor_note") or ""),
        "items": items,
    }
    root = args.site_root / "data" / "breaking"
    write_json(root / "latest.json", payload)
    write_json(root / "archive" / f"{payload['date']}.json", payload)
    print(f"Major developments selected: {len(items)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
