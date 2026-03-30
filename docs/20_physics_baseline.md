# Physics Baseline (Healthy Output Model)

## Question
Given irradiance and temperature, what DC power would a healthy plant produce?

## Model candidates
- Simple linear: \(P_{dc} \\approx \\alpha \\cdot G\) (with clipping)
- Piecewise: low-light + linear mid-range + saturation near inverter limit
- Temperature-adjusted: \(P_{dc}(t) \\propto G(t)\\cdot (1+\\gamma\\,(T_{mod}(t)-T_{ref}))\)

## Constraints (physics-aware)
- \(P_{dc} \\ge 0\)
- Night-time: \(G \\approx 0 \\Rightarrow P_{dc} \\approx 0\)
- Saturation near nameplate/inverter limit
- Hysteresis artifacts are suspicious (often data issues)

## Validation
- Fit on “clean” days; verify on held-out days
- Compare Plant1 vs Plant2 residual distributions

## Outputs
- Baseline fit parameters and units
- Residual plots and error metrics saved to `reports/`
