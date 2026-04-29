"""
Extract voter names from an authorized Montana voter-file export.

This script intentionally does not scrape VoteRef. VoteRef's terms prohibit
unauthorized automated collection/screen scraping, and voter records contain
personal data. Use a Montana voter file you are authorized to access as the source data, then run:

    python VoterRef_Montana_Data.py path\to\montana_voters.csv

The destination output defaults to montana_voter_names.csv with one column: name.
CSV, TSV/TXT, and simple XLSX workbooks are supported with the Python standard
library only.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import zipfile
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional, Tuple
from xml.etree import ElementTree as ET


DEFAULT_OUTPUT = "montana_voter_names.csv"

FIRST_NAME_FIELDS = (
    "first_name",
    "firstname",
    "first name",
    "voter_first_name",
    "voter first name",
    "given_name",
    "given name",
)
MIDDLE_NAME_FIELDS = (
    "middle_name",
    "middlename",
    "middle name",
    "middle_initial",
    "middle initial",
    "mi",
    "voter_middle_name",
    "voter middle name",
)
LAST_NAME_FIELDS = (
    "last_name",
    "lastname",
    "last name",
    "voter_last_name",
    "voter last name",
    "surname",
)
FULL_NAME_FIELDS = (
    "name",
    "full_name",
    "full name",
    "voter_name",
    "voter name",
)


def normalize_header(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.strip().lower()).strip()


def compact_key(value: str) -> str:
    return normalize_header(value).replace(" ", "_")


def first_present(row: Dict[str, str], candidates: Iterable[str]) -> str:
    normalized = {compact_key(key): value for key, value in row.items()}
    spaced = {normalize_header(key): value for key, value in row.items()}

    for candidate in candidates:
        key = compact_key(candidate)
        if key in normalized and normalized[key].strip():
            return normalized[key].strip()

        spaced_key = normalize_header(candidate)
        if spaced_key in spaced and spaced[spaced_key].strip():
            return spaced[spaced_key].strip()

    return ""


def build_name(row: Dict[str, str]) -> str:
    full_name = first_present(row, FULL_NAME_FIELDS)
    if full_name:
        return clean_name(full_name)

    first = first_present(row, FIRST_NAME_FIELDS)
    middle = first_present(row, MIDDLE_NAME_FIELDS)
    last = first_present(row, LAST_NAME_FIELDS)
    return clean_name(" ".join(part for part in (first, middle, last) if part))


def clean_name(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip(" ,;\t\r\n")


def detect_dialect(path: Path) -> csv.Dialect:
    sample = path.read_text(encoding="utf-8-sig", errors="replace")[:8192]
    try:
        return csv.Sniffer().sniff(sample, delimiters=",\t|;")
    except csv.Error:
        dialect = csv.excel_tab if path.suffix.lower() in {".tsv", ".txt"} else csv.excel
        return dialect


def iter_delimited_rows(path: Path) -> Iterator[Dict[str, str]]:
    dialect = detect_dialect(path)
    with path.open("r", newline="", encoding="utf-8-sig", errors="replace") as infile:
        reader = csv.DictReader(infile, dialect=dialect)
        for row in reader:
            yield {key or "": value or "" for key, value in row.items()}


def cell_reference_to_index(cell_reference: str) -> int:
    letters = "".join(ch for ch in cell_reference if ch.isalpha()).upper()
    index = 0
    for letter in letters:
        index = index * 26 + (ord(letter) - ord("A") + 1)
    return max(index - 1, 0)


def read_shared_strings(workbook: zipfile.ZipFile) -> List[str]:
    try:
        data = workbook.read("xl/sharedStrings.xml")
    except KeyError:
        return []

    namespace = {"main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    root = ET.fromstring(data)
    strings: List[str] = []
    for item in root.findall("main:si", namespace):
        pieces = [text.text or "" for text in item.findall(".//main:t", namespace)]
        strings.append("".join(pieces))
    return strings


def read_xlsx_cell(cell: ET.Element, shared_strings: List[str]) -> str:
    namespace = {"main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    cell_type = cell.attrib.get("t")

    if cell_type == "inlineStr":
        pieces = [text.text or "" for text in cell.findall(".//main:t", namespace)]
        return "".join(pieces)

    value = cell.find("main:v", namespace)
    if value is None or value.text is None:
        return ""

    if cell_type == "s":
        try:
            return shared_strings[int(value.text)]
        except (IndexError, ValueError):
            return ""

    return value.text


def iter_xlsx_rows(path: Path) -> Iterator[Dict[str, str]]:
    namespace = {"main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    with zipfile.ZipFile(path) as workbook:
        shared_strings = read_shared_strings(workbook)
        worksheet_names = sorted(
            name for name in workbook.namelist() if re.match(r"xl/worksheets/sheet\d+\.xml$", name)
        )
        if not worksheet_names:
            raise ValueError(f"No worksheets found in {path}")

        rows = ET.fromstring(workbook.read(worksheet_names[0])).findall(".//main:row", namespace)

    header: Optional[List[str]] = None
    for row in rows:
        cells: List[str] = []
        for cell in row.findall("main:c", namespace):
            index = cell_reference_to_index(cell.attrib.get("r", "A1"))
            while len(cells) <= index:
                cells.append("")
            cells[index] = read_xlsx_cell(cell, shared_strings)

        if header is None:
            header = [clean_name(value) for value in cells]
            continue

        if not any(clean_name(value) for value in cells):
            continue

        yield {
            header[index] if index < len(header) and header[index] else f"column_{index + 1}": value
            for index, value in enumerate(cells)
        }


def iter_rows(path: Path) -> Iterator[Dict[str, str]]:
    suffix = path.suffix.lower()
    if suffix == ".xlsx":
        yield from iter_xlsx_rows(path)
    elif suffix in {".csv", ".tsv", ".txt"}:
        yield from iter_delimited_rows(path)
    else:
        raise ValueError("Input must be a .csv, .tsv, .txt, or .xlsx file.")


def write_names(input_path: Path, output_path: Path) -> Tuple[int, int]:
    names_written = 0
    rows_seen = 0
    with output_path.open("w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["name"])

        for row in iter_rows(input_path):
            rows_seen += 1
            name = build_name(row)
            if not name:
                continue

            writer.writerow([name])
            names_written += 1

    return rows_seen, names_written


def list_candidate_sources(directory: Path) -> List[Path]:
    return sorted(
        path
        for path in directory.iterdir()
        if path.is_file()
        and path.suffix.lower() in {".csv", ".tsv", ".txt", ".xlsx"}
        and path.name != DEFAULT_OUTPUT
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Extract names from an authorized Montana voter-file CSV/TSV/TXT/XLSX "
            f"source export into {DEFAULT_OUTPUT}."
        )
    )
    parser.add_argument(
        "input_file",
        type=Path,
        nargs="?",
        help="Source file containing voter data. This is not the blank destination CSV.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path(DEFAULT_OUTPUT),
        help=f"Output CSV path. Default: {DEFAULT_OUTPUT}",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.input_file is None:
        print(
            "Missing source data file. The blank destination is "
            f"{Path(DEFAULT_OUTPUT).resolve()}, but the script also needs a CSV/XLSX "
            "that already contains voter rows.",
            file=sys.stderr,
        )
        candidates = list_candidate_sources(Path.cwd())
        if candidates:
            print("Candidate source files in this folder:", file=sys.stderr)
            for candidate in candidates:
                print(f"  {candidate.name}", file=sys.stderr)
        return 1

    input_path = args.input_file.expanduser().resolve()
    output_path = args.output.expanduser().resolve()

    if not input_path.exists():
        print(
            f"Source data file not found: {input_path}. "
            f"The output destination is {output_path}.",
            file=sys.stderr,
        )
        return 1

    try:
        rows_seen, names_written = write_names(input_path, output_path)
    except Exception as exc:
        print(f"Could not extract names: {exc}", file=sys.stderr)
        return 1

    if rows_seen == 0:
        print(
            f"No data rows found in {input_path}. "
            "Check that the file is the actual voter export, not a blank workbook.",
            file=sys.stderr,
        )
        return 1

    if names_written == 0:
        print(
            f"Read {rows_seen:,} data rows but could not find name columns. "
            "Expected a full-name column or first/middle/last-name columns.",
            file=sys.stderr,
        )
        return 1

    print(f"Wrote {names_written:,} names to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
