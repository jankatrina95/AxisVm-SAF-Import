from pathlib import Path

import pytest
from openpyxl import Workbook

from axisvm_saf_import import read_saf
from axisvm_saf_import.cli import main


@pytest.fixture
def saf_file(tmp_path: Path) -> Path:
    wb = Workbook()
    ws = wb.active
    ws.title = "StructuralMaterial"
    ws.append(["Name", "Type", "Quality"])
    ws.append(["S235", "Steel", "S235"])
    ws.append([None, None, None])
    ws.append(["S355", "Steel", "S355"])
    wb.create_sheet("Leer")
    path = tmp_path / "modell.xlsx"
    wb.save(path)
    return path


def test_read_saf_reads_rows_and_skips_empty(saf_file: Path) -> None:
    model = read_saf(saf_file)
    rows = model.rows("StructuralMaterial")
    assert [r["Name"] for r in rows] == ["S235", "S355"]
    assert model.summary() == {"StructuralMaterial": 2, "Leer": 0}


def test_missing_sheet_gives_empty_list(saf_file: Path) -> None:
    assert read_saf(saf_file).rows("StructuralCurveMember") == []


def test_missing_file_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        read_saf(tmp_path / "fehlt.xlsx")


def test_cli_lists_sheets(saf_file: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main([str(saf_file)]) == 0
    out = capsys.readouterr().out
    assert "StructuralMaterial" in out
    assert "2 Zeilen" in out
