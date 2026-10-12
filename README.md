# axisvm-saf-import

Import von SAF-Dateien (Structural Analysis Format, `.xlsx`) nach AxisVM.

## Stand

- **SAF lesen:** fertig, generisch — jedes Arbeitsblatt wird als Liste von Zeilen
  (Spaltenkopf → Wert) eingelesen.
- **Nach AxisVM schreiben:** noch offen. `axisvm_writer.py` ist ein Platzhalter.
  AxisVM-COM-Member werden erst eingetragen, wenn sie in der AxisVM-API-Doku
  belegt sind (Regel: API-Member nie erfinden).

Details und naechste Schritte: [`PROGRESS.md`](PROGRESS.md).

## Installation

```bash
python -m pip install -e .[dev]
```

## Nutzung

```bash
# Uebersicht: welche SAF-Blaetter mit wie vielen Zeilen
axisvm-saf-import modell.xlsx
```

## Tests

```bash
python -m pytest
```
