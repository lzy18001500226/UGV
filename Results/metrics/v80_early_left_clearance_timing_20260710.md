# v80 Early Left-Clearance Timing

Status: invalid_diagnostic_draft_do_not_use_for_source_edit

Offline analysis of saved `extra_timeseries.csv`; no MWORKS rerun.

Warning: this temporary parser did not reliably bind repeated `Time` columns in
`extra_timeseries.csv`; several `first time/s` values appear to mirror signal
values rather than real simulation time. Do not use this file as a source-edit
gate. Use `summarize_signal_windows.py` / `analyze_ctrlalloc_contributions.py`
outputs instead.

## v80_t1
| dl threshold | first time/s | df | dr | speed | steer | steer_pp | steer_oa |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.45 | 1.371 | 1.371 | 0.6059 | 0.5122 | 0.4096 | 0.1139 | 0.6 |
| 0.3 | 1.337 | 1.337 | 0.4261 |  |  |  |  |
| 0.2 | 2.057 | 2.057 | 0.3021 |  |  |  |  |
| 0.16 | 2.055 | 2.055 | 0.2601 |  |  |  |  |
| 0.12 | 2.051 | 2.051 | 0.2157 |  |  |  |  |
| 0.1 | 2.05 | 2.05 | 0.1945 |  |  |  |  |

min dl sample: t=2.047, dl=0.0007803, df=2.047, dr=0.09683, speed=, steer=

## v80_t2
| dl threshold | first time/s | df | dr | speed | steer | steer_pp | steer_oa |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.45 | 2.101 | 2.101 | 0.611 | 0.5224 | 0.1816 | -0.2205 | 0.6 |
| 0.3 | 2.076 | 2.076 | 0.1317 | 0.5029 | 0.1279 | -0.3423 | 0.6 |
| 0.2 | 2.053 | 2.053 | 0.361 | 0.2593 | 0.005385 | -0.5836 | 0.6 |
| 0.16 | 2.052 | 2.052 | 0.3212 | 0.2599 | 0.004426 | -0.5852 | 0.6 |
| 0.12 | 2.051 | 2.051 | 0.2813 | 0.2595 | 0.00385 | -0.5866 | 0.6 |
| 0.1 | 2.052 | 2.052 | 0.2621 | 0.2533 | 0.005366 | -0.5873 | 0.6 |

min dl sample: t=2.051, dl=0.0001261, df=2.051, dr=0.1629, speed=0.2546, steer=0.003333

## v80_t3
| dl threshold | first time/s | df | dr | speed | steer | steer_pp | steer_oa |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.45 | 0.001076 | 0.001076 | 0.006043 | 0.5063 | 0.1555 | -0.2838 | 0.6 |
| 0.3 | 0.001076 | 0.001076 | 0.006043 | 0.5063 | 0.1555 | -0.2838 | 0.6 |
| 0.2 | 0.001076 | 0.001076 | 0.006043 | 0.5063 | 0.1555 | -0.2838 | 0.6 |
| 0.16 | 2.05 | 2.05 | 0.3242 | 0.2539 | 0.01307 | -0.5715 | 0.6 |
| 0.12 | 2.05 | 2.05 | 0.2823 | 0.2519 | 0.01302 | -0.5729 | 0.6 |
| 0.1 | 2.05 | 2.05 | 0.2623 | 0.2598 | 0.01035 | -0.5734 | 0.6 |

min dl sample: t=2.05, dl=0.0008133, df=2.05, dr=0.1641, speed=0.2516, steer=0.01141

## v80_t4
| dl threshold | first time/s | df | dr | speed | steer | steer_pp | steer_oa |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.45 | 2.127 | 2.127 | 0.1175 | 0.5346 | 0.1833 | -0.2072 | 0.6 |
| 0.3 | 2.127 | 2.127 | 0.1175 | 0.5346 | 0.1833 | -0.2072 | 0.6 |
| 0.2 | 2.056 | 2.056 | 0.3613 | 0.2597 | 0.009819 | -0.5745 | 0.6 |
| 0.16 | 2.054 | 2.054 | 0.3216 | 0.2516 | 0.01091 | -0.5772 | 0.6 |
| 0.12 | 2.053 | 2.053 | 0.2816 | 0.2604 | 0.007144 | -0.5795 | 0.6 |
| 0.1 | 2.052 | 2.052 | 0.2615 | 0.2536 | 0.008548 | -0.5807 | 0.6 |

min dl sample: t=2.051, dl=0.0003151, df=2.051, dr=0.1633, speed=0.2559, steer=0.005519
