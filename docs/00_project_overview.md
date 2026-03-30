# Solar Yield & Fault Diagnostic Engine

## Mission
Build a diagnostic system that explains why a solar plant is underperforming, distinguishing:
- Environmental effects (weather / irradiance variability)
- Hardware issues (sensor/inverter faults, comms dropouts)
- Physical degradation (persistent performance drift)

## R&D pipeline
1. **Data audit**: integrity checks on raw CSVs (ghosts, missing timestamps, saturation, mismatched series).
2. **Physics baseline**: expected \(P_{dc}\) vs irradiance relationship for a healthy plant.
3. **Efficiency analysis**: \(\\eta_{dc}(t)=\\frac{P_{dc}(t)}{G(t)}\) and temperature dependence.
4. **Comparative diagnostics**: Plant1 vs Plant2 to isolate plant-specific failures vs shared weather.

## Repo structure
- `data/`: raw and cleaned data (define conventions per dataset)
- `notebooks/`: exploration notebooks
- `src/`: reusable modules (promoted from notebooks)
- `docs/`: written artifacts for each milestone
- `reports/`: generated outputs (figures, tables)
