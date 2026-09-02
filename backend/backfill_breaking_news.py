#!/usr/bin/env python3
"""Prepare and apply dated major-development backfills from existing archives."""

from __future__ import annotations

import argparse
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from build_breaking_candidates import build
from daily_digest import load_json, write_json


def dates_between(start: date, end: date) -> list[date]:
    if end < start:
        raise ValueError("end date precedes start date")
    return [start + timedelta(days=offset) for offset in range((end - start).days + 1)]


def compact(item: dict[str, Any]) -> dict[str, Any]:
    text = str(item.get("abstract_or_text") or item.get("abstract_zh") or "")
    return {
        "id": str(item.get("id") or ""),
        "channel": str(item.get("channel") or ""),
        "source": str(item.get("source") or ""),
        "source_status": str(item.get("source_status") or item.get("publication_status") or ""),
        "item_type": str(item.get("item_type") or ""),
        "title": str(item.get("title") or ""),
        "summary_zh": str(item.get("summary_zh") or ""),
        "why_it_matters_zh": str(item.get("why_it_matters_zh") or ""),
        "abstract_excerpt": text[:450],
        "quality_score": item.get("quality_score"),
        "editorial_score": item.get("editorial_score"),
        "url": str(item.get("url") or ""),
        "published_at": str(item.get("published_at") or ""),
        "creators": item.get("creators") or [],
        "metrics": item.get("metrics") or {},
        "metadata": item.get("metadata") or {},
    }


def shortlist(items: list[dict[str, Any]], limit: int = 20) -> list[dict[str, Any]]:
    ordered = sorted(
        items,
        key=lambda item: (
            int(item.get("editorial_score") or 0),
            float(item.get("quality_score") or 0),
            str(item.get("published_at") or ""),
        ),
        reverse=True,
    )
    chosen: list[dict[str, Any]] = []
    seen: set[str] = set()
    for channel in ("aixchem", "aixbio", "aixmath", "aivoices", "engineering"):
        for item in (value for value in ordered if value.get("channel") == channel):
            item_id = str(item.get("id") or "")
            if item_id and item_id not in seen:
                chosen.append(item)
                seen.add(item_id)
            if sum(value.get("channel") == channel for value in chosen) >= 4:
                break
    for item in ordered:
        item_id = str(item.get("id") or "")
        if item_id and item_id not in seen:
            chosen.append(item)
            seen.add(item_id)
        if len(chosen) >= limit:
            break
    return chosen[:limit]


def prepare(root: Path, site_root: Path, start: date, end: date, output: Path) -> dict[str, Any]:
    full_root = output.parent / "candidates"
    days = []
    for run_date in dates_between(start, end):
        payload = build(root, site_root, run_date, write_latest=False)
        write_json(full_root / f"{run_date}.json", payload)
        days.append({
            "date": run_date.isoformat(),
            "candidate_count": payload.get("count", 0),
            "items": [compact(item) for item in shortlist(payload.get("items") or [])],
        })
    result = {
        "schema_version": "1.0",
        "start_date": start.isoformat(),
        "end_date": end.isoformat(),
        "days": days,
    }
    write_json(output, result)
    return result


def breaking_item(source: dict[str, Any], selected: dict[str, Any], rank: int) -> dict[str, Any]:
    return {
        "id": str(source.get("id") or ""),
        "rank": rank,
        "channel": str(source.get("channel") or "aivoices"),
        "source": str(source.get("source") or ""),
        "source_status": str(source.get("source_status") or source.get("publication_status") or "reported_result"),
        "item_type": str(source.get("item_type") or "update"),
        "headline_zh": str(selected.get("headline_zh") or source.get("title") or ""),
        "summary_zh": str(selected.get("summary_zh") or source.get("summary_zh") or ""),
        "why_breaking_zh": str(selected.get("why_breaking_zh") or ""),
        "url": str(source.get("url") or ""),
        "published_at": str(source.get("published_at") or ""),
        "creators": source.get("creators") or [],
        "metrics": source.get("metrics") or {},
        "metadata": source.get("metadata") or {},
    }


def update_daily_archive(site_root: Path, run_date: str, items: list[dict[str, Any]]) -> None:
    for relative in (
        Path("data") / "daily" / "archive" / f"{run_date}.json",
        Path("data") / "archive" / f"{run_date}.json",
    ):
        path = site_root / relative
        if not path.exists():
            continue
        payload = load_json(path, {})
        payload["breaking_news"] = items
        write_json(path, payload)


def apply(site_root: Path, candidates_root: Path, curation_path: Path) -> tuple[int, int]:
    curation = load_json(curation_path, {})
    days = curation.get("days") or []
    expected = {path.stem for path in candidates_root.glob("*.json")}
    supplied = [str(day.get("date") or "") for day in days]
    if len(supplied) != len(set(supplied)):
        raise RuntimeError("Backfill output contains duplicate dates")
    missing = sorted(expected - set(supplied))
    if missing:
        raise RuntimeError(f"Backfill output is missing dates: {', '.join(missing)}")

    total = 0
    batch_ids: set[str] = set()
    batch_urls: set[str] = set()
    for day in days:
        run_date = str(day.get("date") or "")
        candidates = load_json(candidates_root / f"{run_date}.json", {})
        by_id = {str(item.get("id") or ""): item for item in candidates.get("items") or []}
        selected_rows = day.get("selected") or []
        if not 1 <= len(selected_rows) <= 3:
            raise RuntimeError(f"{run_date} must select 1 to 3 items")
        seen: set[str] = set()
        items = []
        for rank, selected in enumerate(selected_rows, 1):
            item_id = str(selected.get("id") or "")
            if not item_id or item_id in seen or item_id not in by_id:
                raise RuntimeError(f"{run_date} has an invalid selected id: {item_id}")
            source_url = str(by_id[item_id].get("url") or "").split("?", 1)[0].rstrip("/").lower()
            if item_id in batch_ids or (source_url and source_url in batch_urls):
                raise RuntimeError(f"{run_date} repeats a selected event in this batch: {item_id}")
            seen.add(item_id)
            batch_ids.add(item_id)
            if source_url:
                batch_urls.add(source_url)
            items.append(breaking_item(by_id[item_id], selected, rank))
        payload = {
            "schema_version": "1.0",
            "date": run_date,
            "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "editor_note": str(day.get("editor_note") or ""),
            "items": items,
        }
        write_json(site_root / "data" / "breaking" / "archive" / f"{run_date}.json", payload)
        update_daily_archive(site_root, run_date, items)
        total += len(items)
    return len(days), total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare_parser = subparsers.add_parser("prepare")
    prepare_parser.add_argument("--root", type=Path, default=Path("."))
    prepare_parser.add_argument("--site-root", type=Path, default=Path("public"))
    prepare_parser.add_argument("--start-date", required=True)
    prepare_parser.add_argument("--end-date", required=True)
    prepare_parser.add_argument("--output", type=Path, required=True)

    apply_parser = subparsers.add_parser("apply")
    apply_parser.add_argument("curation", type=Path)
    apply_parser.add_argument("--site-root", type=Path, default=Path("public"))
    apply_parser.add_argument("--candidates-root", type=Path, required=True)

    args = parser.parse_args()
    if args.command == "prepare":
        result = prepare(
            args.root.resolve(), args.site_root.resolve(), date.fromisoformat(args.start_date),
            date.fromisoformat(args.end_date), args.output.resolve(),
        )
        print(f"Prepared {len(result['days'])} backfill days: {result['start_date']} to {result['end_date']}")
        return 0
    days, items = apply(args.site_root.resolve(), args.candidates_root.resolve(), args.curation.resolve())
    print(f"Applied {items} major developments across {days} days")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
