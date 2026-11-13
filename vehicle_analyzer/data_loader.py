"""Load vehicle telemetry data from CSV files."""

from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "timestamp",
    "speed_kmh",
    "rpm",
    "engine_temp_c",
    "fuel_consumption_l_100km",
}


def load_vehicle_data(file_path: str | Path) -> pd.DataFrame:
    """Load a vehicle telemetry CSV and check that its columns are present.

    Args:
        file_path: Path to the CSV file.

    Returns:
        A pandas DataFrame containing the vehicle telemetry.

    Raises:
        ValueError: If one or more required columns are missing.
    """
    data = pd.read_csv(file_path)
    missing_columns = REQUIRED_COLUMNS - set(data.columns)

    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Missing required columns: {missing}")

    return data
