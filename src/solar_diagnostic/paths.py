from __future__ import annotations

import os
from pathlib import Path

DEFAULT_DATA_ROOT = Path(r"E:\coding\data\Kaggle Solar Power Generation Data")


def get_data_root() -> Path:
    raw = os.environ.get("SOLAR_DATA_ROOT", "").strip()
    if raw:
        return Path(raw)
    return DEFAULT_DATA_ROOT
