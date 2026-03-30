# Kaggle Solar Power Generation Data — Solar Yield & Fault Diagnostic Engine

## Data location (not tracked in git)
Raw CSVs are stored outside this repository at:
- `E:\coding\data\Kaggle Solar Power Generation Data`

You can override the data root via environment variable:
- `SOLAR_DATA_ROOT`

Example (PowerShell):

```powershell
$env:SOLAR_DATA_ROOT = "E:\coding\data\Kaggle Solar Power Generation Data"
uv run python -c "from solar_diagnostic.paths import get_data_root; print(get_data_root())"
```

## Setup
**Python 3.13** is required (`requires-python` in `pyproject.toml`; `.python-version` is for local uv).

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (or `py -m pip install uv`), then from the repo root:

```powershell
uv sync --all-groups
```

This creates or updates `.venv` and installs runtime plus dev tools (`black`, `ruff`). Use `uv run <command>` to run tools and scripts inside the project environment.
