# Efficiency Analysis (Real-time + Temperature Correlation)

## Definition
\[
\\eta_{dc}(t)=\\frac{P_{dc}(t)}{G(t)}
\]

## Notes
- Define the irradiance floor \(G_{min}\) to avoid division artifacts.
- Report units explicitly (often \(\\eta_{dc}\) here is a *proxy*, not true PV efficiency).

## Analyses
- \(\\eta_{dc}\) time series + rolling statistics
- Correlation/regression vs module temperature
- Stratify by irradiance bands (low/medium/high)

## Failure signatures
- Sudden step drop: sensor/inverter fault or curtailment
- Temperature-sensitive drift: thermal coupling changes or degradation
- Persistent plant-only offset vs region-wide: plant-specific issue

## Outputs
- Efficiency vs temperature plots
- Plant1/Plant2 comparative panels
