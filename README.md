# Vehicle Data Analyzer

Vehicle Data Analyzer is a beginner-friendly automotive software portfolio
project built with Python and pandas. In this first step, it loads vehicle
telemetry from a CSV file and verifies that the expected columns are present.

Graphs and anomaly detection are intentionally left for later steps.

## Project structure

```text
vehicle-data-analyzer/
|-- data/
|   `-- sample_vehicle_data.csv
|-- tests/
|   `-- test_data_loader.py
|-- vehicle_analyzer/
|   |-- __init__.py
|   `-- data_loader.py
|-- README.md
`-- requirements.txt
```

- `data/sample_vehicle_data.csv` contains 30 rows of synthetic driving data.
- `vehicle_analyzer/__init__.py` marks the folder as a Python package and
  exposes the loader function.
- `vehicle_analyzer/data_loader.py` loads a CSV with pandas and validates its
  required columns.
- `tests/test_data_loader.py` checks successful loading and missing-column
  validation.
- `requirements.txt` lists the Python packages needed for the project.
- `README.md` explains the project and how to use it.

## Setup

Python 3.10 or newer is recommended.

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux, activate it with:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Load the sample data

Run this command from the project root:

```bash
python -c "from vehicle_analyzer import load_vehicle_data; print(load_vehicle_data('data/sample_vehicle_data.csv').head())"
```

The loader returns a pandas `DataFrame`. It raises a `ValueError` with the
missing column names if the CSV does not have all required telemetry columns.

## Run the tests

```bash
python -m pytest
```
