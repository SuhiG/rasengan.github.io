#!/usr/bin/env python3
"""Fetch publication metadata from a Google Scholar author profile and write Jekyll data YAML."""

from __future__ import annotations

import argparse
import html
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import List
from urllib.parse import parse_qs, urlencode, urljoin, urlparse
from urllib.request import Request, urlopen

SCHOLAR_BASE_URL = "https://scholar.google.com/citations"
DEFAULT_PAGESIZE = 100


@dataclass
class Publication:
    title: str
    authors: str
    venue: str
    year: int | None
    scholar_url: str


@dataclass
class ScholarStats:
    citations: int
    h_index: int
    i10_index: int


def _strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"\s+", " ", value).strip()
    return html.unescape(value)


def _extract_rows(page_html: str) -> List[str]:
    return re.findall(r"<tr[^>]*class=['\"][^'\"]*\bgsc_a_tr\b[^'\"]*['\"][^>]*>(.*?)</tr>", page_html, flags=re.DOTALL)


def _extract_publications_from_page(page_html: str) -> List[Publication]:
    publications: List[Publication] = []
    rows = _extract_rows(page_html)

    for row_html in rows:
        title_match = re.search(
            r"<a(?=[^>]*\bclass=['\"][^'\"]*\bgsc_a_at\b[^'\"]*['\"])(?=[^>]*\bhref=['\"]([^'\"]+)['\"])[^>]*>(.*?)</a>",
            row_html,
            flags=re.DOTALL,
        )
        meta_matches = re.findall(r"<div[^>]*class=['\"][^'\"]*\bgs_gray\b[^'\"]*['\"][^>]*>(.*?)</div>", row_html, flags=re.DOTALL)
        year_match = re.search(r"<td[^>]*class=['\"][^'\"]*\bgsc_a_y\b[^'\"]*['\"][^>]*>.*?(\d{4})", row_html, flags=re.DOTALL)

        if not title_match:
            continue

        scholar_url = urljoin("https://scholar.google.com", html.unescape(title_match.group(1)))
        title = _strip_tags(title_match.group(2))
        authors = _strip_tags(meta_matches[0]) if len(meta_matches) > 0 else ""
        venue = _strip_tags(meta_matches[1]) if len(meta_matches) > 1 else ""
        year = int(year_match.group(1)) if year_match else None

        if title:
            publications.append(
                Publication(
                    title=title,
                    authors=authors,
                    venue=venue,
                    year=year,
                    scholar_url=scholar_url,
                )
            )

    return publications


def _extract_stats(page_html: str) -> ScholarStats:
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", page_html, flags=re.DOTALL)
    stats_map: dict[str, int] = {}

    for row_html in rows:
        label_match = re.search(r"<a[^>]*class=['\"][^'\"]*\bgsc_rsb_f\b[^'\"]*['\"][^>]*>(.*?)</a>", row_html, flags=re.DOTALL)
        value_match = re.search(r"<td[^>]*class=['\"][^'\"]*\bgsc_rsb_std\b[^'\"]*['\"][^>]*>(.*?)</td>", row_html, flags=re.DOTALL)

        if not label_match or not value_match:
            continue

        label = _strip_tags(label_match.group(1)).lower().replace("-", "").replace(" ", "")
        value_text = _strip_tags(value_match.group(1)).replace(",", "")

        if not value_text.isdigit():
            continue

        stats_map[label] = int(value_text)

    if "citations" not in stats_map or "hindex" not in stats_map or "i10index" not in stats_map:
        # Fallback for alternate markup where classes are changed/obfuscated.
        stat_values = [int(value.replace(",", "")) for value in re.findall(r"id=['\"]gsc_rsb_st\d+['\"][^>]*>(\d[\d,]*)<", page_html)[:3]]
        if len(stat_values) == 3:
            stats_map.setdefault("citations", stat_values[0])
            stats_map.setdefault("hindex", stat_values[1])
            stats_map.setdefault("i10index", stat_values[2])

    try:
        return ScholarStats(
            citations=stats_map["citations"],
            h_index=stats_map["hindex"],
            i10_index=stats_map["i10index"],
        )
    except KeyError as exc:
        raise ValueError("Unable to parse Google Scholar stats from the profile page.") from exc


def _fetch_html(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            )
        },
    )
    with urlopen(request, timeout=30) as response:  # noqa: S310
        return response.read().decode("utf-8", errors="replace")


def fetch_publications(user_id: str, hl: str = "en", delay_s: float = 1.0) -> List[Publication]:
    cstart = 0
    publications: List[Publication] = []

    while True:
        query = {
            "user": user_id,
            "hl": hl,
            "view_op": "list_works",
            "sortby": "pubdate",
            "cstart": cstart,
            "pagesize": DEFAULT_PAGESIZE,
        }
        page_html = _fetch_html(f"{SCHOLAR_BASE_URL}?{urlencode(query)}")
        page_publications = _extract_publications_from_page(page_html)

        if not page_publications:
            break

        publications.extend(page_publications)

        if len(page_publications) < DEFAULT_PAGESIZE:
            break

        cstart += DEFAULT_PAGESIZE
        time.sleep(delay_s)

    deduped: List[Publication] = []
    seen = set()
    for publication in publications:
        key = publication.title.lower().strip()
        if key and key not in seen:
            seen.add(key)
            deduped.append(publication)

    return deduped


def fetch_stats(user_id: str, hl: str = "en") -> ScholarStats:
    query = {
        "user": user_id,
        "hl": hl,
    }
    page_html = _fetch_html(f"{SCHOLAR_BASE_URL}?{urlencode(query)}")
    return _extract_stats(page_html)


def user_id_from_url(profile_url: str) -> str:
    parsed = urlparse(profile_url)
    user_values = parse_qs(parsed.query).get("user", [])
    if not user_values or not user_values[0]:
        raise ValueError("Google Scholar URL must contain a non-empty 'user' query parameter.")
    return user_values[0]


def _yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def write_yaml(publications: List[Publication], output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    for publication in publications:
        lines.append(f"- title: {_yaml_quote(publication.title)}")
        lines.append(f"  authors: {_yaml_quote(publication.authors)}")
        lines.append(f"  venue: {_yaml_quote(publication.venue)}")
        lines.append(f"  year: {publication.year if publication.year is not None else 'null'}")
        lines.append(f"  scholar_url: {_yaml_quote(publication.scholar_url)}")

    output_file.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def write_stats_yaml(stats: ScholarStats, output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"citations: {stats.citations}",
        f"h_index: {stats.h_index}",
        f"i10_index: {stats.i10_index}",
    ]
    output_file.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Google Scholar publications into a Jekyll data file.")
    parser.add_argument("--profile-url", required=True)
    parser.add_argument("--output", default="_data/google_scholar_publications.yml")
    parser.add_argument("--stats-output", default="_data/google_scholar_stats.yml")
    parser.add_argument("--hl", default="en")
    args = parser.parse_args()

    try:
        user_id = user_id_from_url(args.profile_url)
        publications = fetch_publications(user_id=user_id, hl=args.hl)
        stats = fetch_stats(user_id=user_id, hl=args.hl)
        write_yaml(publications, Path(args.output))
        write_stats_yaml(stats, Path(args.stats_output))
        print(f"Wrote {len(publications)} publications to {args.output}")
        print(f"Wrote Google Scholar stats to {args.stats_output}")
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
