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


def _strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"\s+", " ", value).strip()
    return html.unescape(value)


def _extract_rows(page_html: str) -> List[str]:
    return re.findall(r'<tr class="gsc_a_tr">(.*?)</tr>', page_html, flags=re.DOTALL)


def _extract_publications_from_page(page_html: str) -> List[Publication]:
    publications: List[Publication] = []
    rows = _extract_rows(page_html)

    for row_html in rows:
        title_match = re.search(r'<a class="gsc_a_at" href="([^"]+)">(.*?)</a>', row_html, flags=re.DOTALL)
        meta_matches = re.findall(r'<div class="gs_gray">(.*?)</div>', row_html, flags=re.DOTALL)
        year_match = re.search(r'<td class="gsc_a_y">.*?<span[^>]*>(\d{4})</span>', row_html, flags=re.DOTALL)

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


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Google Scholar publications into a Jekyll data file.")
    parser.add_argument("--profile-url", required=True)
    parser.add_argument("--output", default="_data/google_scholar_publications.yml")
    parser.add_argument("--hl", default="en")
    args = parser.parse_args()

    try:
        user_id = user_id_from_url(args.profile_url)
        publications = fetch_publications(user_id=user_id, hl=args.hl)
        write_yaml(publications, Path(args.output))
        print(f"Wrote {len(publications)} publications to {args.output}")
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
