"""Kommandozeile: SAF-Datei einlesen und Uebersicht ausgeben."""

from __future__ import annotations

import argparse
import sys

from .saf_reader import read_saf


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="axisvm-saf-import",
        description="SAF-Datei (.xlsx) einlesen und Inhalt auflisten.",
    )
    parser.add_argument("datei", help="Pfad zur SAF-.xlsx-Datei")
    args = parser.parse_args(argv)

    try:
        model = read_saf(args.datei)
    except FileNotFoundError as exc:
        print(f"Fehler: {exc}", file=sys.stderr)
        return 1

    print(f"SAF-Datei: {model.source}")
    for name, count in model.summary().items():
        print(f"  {name:<40} {count:>6} Zeilen")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
