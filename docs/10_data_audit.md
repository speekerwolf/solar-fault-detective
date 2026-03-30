# Data Audit (Integrity + Ghost Detection)

## Question
Do the raw time series support physics-consistent diagnostics without hidden artifacts?

## Data contracts
- **Time zone**:
- **Sampling cadence**:
- **Keys**: Plant, inverter, string, sensor identifiers
- **Units**: Irradiance \(G\) [W/m²], DC power \(P_{dc}\) [W], module temp [°C], etc.

## Integrity checks (minimum)
- Missing timestamps / gaps (by key)
- Duplicated timestamps
- Time shifts / clock drift between sensors
- Saturation / clipping (flat tops at sensor max)
- Flatlines / stuck-at values
- Impossible ramps (rate-of-change outliers)
- Mismatched time series alignment across columns (e.g., irradiance present while power missing)

## Cleaning policy
- What is dropped vs imputed vs flagged?
- How are “unknown” states represented?

## Outputs
- Summary table of anomaly counts by plant/inverter
- A small set of high-signal plots saved to `reports/figures/`
