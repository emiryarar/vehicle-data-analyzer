"""Tests for the vehicle telemetry data loader."""

from pathlib import Path

import pytest

from vehicle_analyzer.data_loader import REQUIRED_COLUMNS, load_vehicle_data


SAMPLE_DATA_FILE = (
    Path(__file__).resolve().parents[1] / "data" / "sample_vehicle_data.csv"
)


def test_load_sample_vehicle_data() -> None:
    data = load_vehicle_data(SAMPLE_DATA_FILE)

    assert len(data) == 30
    assert REQUIRED_COLUMNS.issubset(data.columns)


def test_missing_required_column_raises_error(tmp_path: Path) -> None:
    incomplete_file = tmp_path / "incomplete_data.csv"
    incomplete_file.write_text("timestamp,speed_kmh\n2026-01-15T08:00:00,0\n")

    with pytest.raises(ValueError, match="Missing required columns"):
        load_vehicle_data(incomplete_file)
