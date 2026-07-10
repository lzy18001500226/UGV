# v78 Gap-Side Screening On v74 Saved Signals

Status: offline_screening_only_timeaxis_corrected, 2026-07-10 CST

This is offline analysis of saved `extra_timeseries.csv` files using per-signal left-side `Time` binding from `summarize_signal_windows.py`. It does not rerun MWORKS and does not edit source.

Condition screened:

```text
flag == 1 and df > 1.5 and min(dl, dr) < 0.15 and abs(dl - dr) > 0.08
```

| Run | Samples | Hit samples | Hit fraction | First hit intervals | Event-window hits |
|---|---:|---:|---:|---|---|
| v74_track1 | 1745 | 152 | 0.08711 | `[[4.28, 4.86], [5.17, 5.82], [9.05, 9.75], [10.1, 10.7]]` | t=4.45: 43/51 |
| v74_track2 | 12002 | 651 | 0.05424 | `[[1.6, 1.74], [4.27, 6.44], [7.54, 8.43], [9.01, 9.33], [9.7, 9.87], [80.45, 80.6], [90.7, 91.5], [91.6, 101.55], [101.65, 104.45]]` | t=4.7: 50/51 |
| v74_track3 | 12002 | 547 | 0.04558 | `[[1.09, 1.22], [4.7, 5.39], [5.69, 6.28], [6.86, 7.08], [7.37, 7.43], [7.69, 7.87], [8.42, 8.64], [9.43, 9.57], [62.65, 62.7], [63.15, 64.6], [64.7, 74.45], [112.9, 113.1]]` | t=1.05: 14/51; t=4.85: 41/51 |
| v74_track4 | 12002 | 644 | 0.05366 | `[[0.8, 0.88], [3.87, 6.04], [7.15, 7.39], [7.62, 8.03], [52.1, 53.0], [53.1, 55.65], [76.35, 79.0], [80.4, 83.15], [83.25, 84.55], [97.05, 97.45], [103.15, 103.25], [103.35, 106.3]]` | t=4.35: 51/51; t=104.0: 11/51 |

## Interpretation

- This condition is not too sparse for the early road-edge event windows:
  Track1/2/3/4 early road events are covered at `43/51`, `50/51`, `41/51`,
  and `51/51` samples respectively.
- It only partially covers Track3's early obstacle event (`14/51`) and Track4's
  late road event (`11/51`), so it cannot explain all remaining v74 losses.
- The condition also appears in later clean or non-target intervals on
  Track2/3/4. It is therefore not a safe direct source-edit gate by itself.
- A source candidate would need an additional narrow guard or a different
  mechanism; do not apply a gap-side source edit from this screening alone.
