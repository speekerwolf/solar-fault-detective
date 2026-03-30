# Comparative Diagnostics (Plant 1 vs Plant 2)

## Question
Is the underperformance plant-specific, or driven by shared weather/regional effects?

## Comparison design
- Align clocks/time zones first.
- Compare:
  - irradiance distributions
  - baseline residuals
  - \(\\eta_{dc}\) distributions
  - anomaly rates (gaps, saturation, flatlines)

## Interpretation guide
- Shared shifts in irradiance + shared drops in power: likely weather.
- Same irradiance but plant-only power loss: likely plant hardware/soiling/degradation.
- Sensor-only anomalies (irradiance flatline): measurement fault masquerading as yield loss.

## Outputs
- A short diagnosis narrative with evidence plots.
