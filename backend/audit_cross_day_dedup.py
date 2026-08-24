#!/usr/bin/env python3
"""Replay cross-day report deduplication over existing combined archives."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date
from pathlib import Path

from aix_pipeline import archive_items, previously_reported_keys, report_key
from daily_digest import load_json


def audit(site_root: Path, dates: list[str]) -> dict:
    seen: set[str] = set()
    days = []
    for day in sorted(dict.fromkeys(dates)):
        path = site_root / "data" / "daily" / "archive" / f"{day}.json"
        payload = load_json(path, {})
        if not payload:
            raise FileNotFoundError(path)
        items = archive_items(payload)
        repeated = []
        kept = []
        for item in items:
            key = report_key(item)
            if key and key in seen:
                repeated.append(item)
                continue
            if key:
                seen.add(key)
            kept.append(item)
        days.append({
            "date": day,
            "selected_before": len(items),
            "repeated": len(repeated),
            "selected_after": len(kept),
            "repeated_by_channel": dict(sorted(Counter(str(item.get("channel") or "unknown") for item in repeated).items())),
            "repeated_ids": [str(item.get("id") or "") for item in repeated],
        })
    return {"dates": days, "remaining_cross_day_duplicates": 0}


def audit_target_date(site_root: Path, day: str) -> dict:
    path = site_root / "data" / "daily" / "archive" / f"{day}.json"
    payload = load_json(path, {})
    if not payload:
        raise FileNotFoundError(path)
    run_date = date.fromisoformat(day)
    historical = previously_reported_keys(site_root, run_date)
    repeated = []
    for item in archive_items(payload):
        key = report_key(item)
        if key and key in historical:
            repeated.append(item)
    return {
        "target_date": day,
        "selected": len(archive_items(payload)),
        "remaining_cross_day_duplicates": len(repeated),
        "repeated_by_channel": dict(sorted(Counter(str(item.get("channel") or "unknown") for item in repeated).items())),
        "repeated_ids": [str(item.get("id") or "") for item in repeated],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dates", nargs="*")
    parser.add_argument("--target-date")
    parser.add_argument("--site-root", type=Path, default=Path("public"))
    args = parser.parse_args()
    if args.target_date:
        result = audit_target_date(args.site_root, args.target_date)
    elif args.dates:
        result = audit(args.site_root, args.dates)
    else:
        parser.error("provide dates or --target-date")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["remaining_cross_day_duplicates"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
