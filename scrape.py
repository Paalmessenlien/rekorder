#!/usr/bin/env python3
"""Scrape gjeldende rekorder fra rekord.bueskyting.no og skriv rekorder.csv.

Bruker kun Python-stdlib (urllib, html, re, csv) — fungerer i GitHub Actions
uten pip install. Henter alle 70 (rundeid × divisjon)-kombinasjoner.
"""
from __future__ import annotations

import csv
import re
import sys
import urllib.request
from datetime import datetime
from html import unescape
from pathlib import Path
from typing import Iterable

DIVISJONER = [
    "Recurve", "Compound", "Barebow", "Langbue", "Tradisjonell",
    "Synshemmede", "PsykiskUtviklingshemmet",
]
RUNDETYPER = [
    (3,  "Skandiarunde"),
    (4,  "Norgesrunde"),
    (5,  "1440-runde"),
    (6,  "1/2 1440-runde"),
    (21, "Norsk kortrunde"),
    (26, "720-runde"),
    (28, "2 x 720-runde"),
    (22, "60 piler 18 m"),
    (23, "60 piler 25 m"),
    (27, "30 piler 18 m"),
]
URL = "https://rekord.bueskyting.no/rekord.php?rundeid={rundeid}&divisjon={divisjon}"

MONTHS = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,  "May": 5,  "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12,
}

KLASSE_RE = re.compile(
    r"<tr>\s*<td\s+colspan=6\s*>\s*<u>([^<]+)</u>\s*</td>\s*</tr>",
    re.IGNORECASE,
)
# Datarad: <tr><td>LABEL:</td><td>NAME, CLUB</td><td align=right>SCORE</td><td align=right>DATE</td>...
ROW_RE = re.compile(
    r"<tr>\s*"
    r"<td[^>]*>\s*([^<:]+?)\s*:\s*</td>\s*"
    r"<td[^>]*>([^<]*)</td>\s*"
    r"<td\s+align=right[^>]*>\s*(\d+)\s*</td>\s*"
    r"<td\s+align=right[^>]*>\s*(\d{1,2}\s+[A-Za-z]+\s+\d{2})\s*</td>",
    re.IGNORECASE,
)
MEMBER_RE = re.compile(
    r"<tr>\s*<td[^>]*>\s*&nbsp[^<]*</td>\s*"
    r"<td\s+colspan=5[^>]*>\s*v/\s*([^<]+?)\s*</td>\s*</tr>",
    re.IGNORECASE,
)


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "rekord-scraper/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()
    # Sida deklarerer windows-1252, men sender faktisk UTF-8.
    return raw.decode("utf-8", errors="replace")


def parse_date(s: str) -> str:
    parts = s.split()
    if len(parts) != 3:
        return ""
    day, mon, yy = parts
    m = MONTHS.get(mon[:3].title())
    if not m:
        return ""
    try:
        yy_int = int(yy)
        d_int = int(day)
    except ValueError:
        return ""
    yyyy = 1900 + yy_int if yy_int >= 50 else 2000 + yy_int
    try:
        return datetime(yyyy, m, d_int).date().isoformat()
    except ValueError:
        return ""


def split_name_club(s: str) -> tuple[str, str]:
    """For individuelle rekorder: 'Name, Club'. For lag: bare 'Club'."""
    s = unescape(s).strip()
    if "," in s:
        name, club = s.split(",", 1)
        return name.strip(), club.strip()
    return "", s


def parse_page(html: str, divisjon: str, rundeid: int, runde_navn: str) -> list[dict]:
    rows: list[dict] = []
    pos = 0
    cur_klasse = ""
    last_record: dict | None = None
    url = URL.format(rundeid=rundeid, divisjon=divisjon)

    while pos < len(html):
        kmatch = KLASSE_RE.search(html, pos)
        rmatch = ROW_RE.search(html, pos)
        mmatch = MEMBER_RE.search(html, pos)
        candidates = [c for c in [kmatch, rmatch, mmatch] if c]
        if not candidates:
            break
        nxt = min(candidates, key=lambda m: m.start())

        if nxt is kmatch:
            cur_klasse = unescape(nxt.group(1)).strip()
            last_record = None
        elif nxt is rmatch:
            label = unescape(nxt.group(1)).strip()
            who = nxt.group(2)
            score = int(nxt.group(3))
            dato = parse_date(nxt.group(4))
            name, club = split_name_club(who)
            rec = {
                "divisjon": divisjon,
                "klasse": cur_klasse,
                "rundeid": rundeid,
                "rundenavn": runde_navn,
                "aspekt": label,
                "score": score,
                "navn": name,
                "klubb": club,
                "medlemmer": "",
                "dato": dato,
                "url": url,
            }
            rows.append(rec)
            last_record = rec
        else:
            members = unescape(nxt.group(1)).strip().rstrip(",").rstrip()
            if last_record is not None:
                last_record["medlemmer"] = members

        pos = nxt.end()

    return rows


def write_meta(out_path: Path, count: int, by_div: dict) -> None:
    import json
    meta = {
        "scraped_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total": count,
        "by_divisjon": by_div,
        "source": "https://rekord.bueskyting.no/",
    }
    out_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def scrape_all(out_path: Path) -> int:
    all_rows: list[dict] = []
    total = len(DIVISJONER) * len(RUNDETYPER)
    n = 0
    for div in DIVISJONER:
        for rid, navn in RUNDETYPER:
            n += 1
            url = URL.format(rundeid=rid, divisjon=div)
            print(f"[{n:>2}/{total}] {div:<28} runde {rid:>2} {navn}", flush=True)
            try:
                html = fetch(url)
            except Exception as e:
                print(f"  ! feil: {e}", file=sys.stderr)
                continue
            rows = parse_page(html, div, rid, navn)
            all_rows.extend(rows)
            print(f"     -> {len(rows)} rekorder")

    fields = [
        "divisjon", "klasse", "rundeid", "rundenavn", "aspekt",
        "score", "navn", "klubb", "medlemmer", "dato", "url",
    ]
    # Sorter for stabile diffs
    all_rows.sort(key=lambda r: (
        r["divisjon"], r["rundeid"], r["klasse"], r["aspekt"]
    ))
    with out_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(all_rows)

    by_div: dict[str, int] = {}
    for r in all_rows:
        by_div[r["divisjon"]] = by_div.get(r["divisjon"], 0) + 1
    meta_path = out_path.with_name(out_path.stem + "-meta.json")
    write_meta(meta_path, len(all_rows), by_div)

    print(f"\nSkrev {len(all_rows)} rekorder til {out_path}")
    print(f"Skrev metadata til {meta_path}")
    return len(all_rows)


def main() -> int:
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "rekorder.csv")
    return 0 if scrape_all(out) > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
