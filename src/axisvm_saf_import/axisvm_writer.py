"""Uebertragung eines SafModel nach AxisVM (Platzhalter).

Bewusst leer: AxisVM-COM-Member werden erst eingetragen, wenn sie in der
AxisVM-Programmierdokumentation belegt sind. Keine geratenen API-Aufrufe.
"""

from __future__ import annotations

from .saf_reader import SafModel


def write_to_axisvm(model: SafModel) -> None:
    """Schreibt das Modell in eine laufende AxisVM-Instanz."""
    raise NotImplementedError(
        "AxisVM-Anbindung noch nicht umgesetzt (siehe PROGRESS.md, Punkt 2)."
    )
