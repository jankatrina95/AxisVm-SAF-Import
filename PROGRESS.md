# PROGRESS — axisvm-saf-import

Source of Truth fuer den Projektstand.

## Erledigt (2026-10-12)
- Repo-Grundgeruest: `pyproject.toml`, Paket `src/axisvm_saf_import`, Tests.
- `saf_reader.read_saf()`: liest alle Blaetter einer SAF-`.xlsx` generisch ein.
- CLI `axisvm-saf-import <datei>`: listet Blaetter und Zeilenanzahl.

## Offen
1. Zuordnung SAF-Blaetter → AxisVM-Objekte festlegen
   (Material, Querschnitt, Knoten, Stab, Lager, Lastfaelle, Lasten).
2. AxisVM-COM-Anbindung (`axisvm_writer.py`) — nur mit belegten API-Membern
   aus der AxisVM-Programmierdoku.
3. Einheiten-Pruefung (SAF-Einheiten vs. AxisVM-Modelleinheiten).
4. Import-Protokoll auf Deutsch (was uebernommen, was uebersprungen).
5. Abgleich mit dem bestehenden SAF-Tool `axisvm-frilo-saf` — gemeinsamen
   SAF-Leser wiederverwenden statt doppeln?
