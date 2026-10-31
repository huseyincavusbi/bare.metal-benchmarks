# bare.metal - benchmark results

Results produced by `bench/run_benchmark.sh` in
[bare.metal](https://github.com/huseyincavusbi/bare.metal).

Every folder under `runs/` contains `run.json` (provenance),
`grand.json` (all models x engines x formats), per-model/engine slices,
`summary.md`, `energy/` (trimmed powermetrics logs, previewable) and
`energy-raw.tar.gz` (full raw logs).

## Scoreboard

| run | ver | model | fmt | bare.metal pre / dec | best pre / dec (engine) | gap |
|---|---|---|---|---|---|---|
| [`10-17-2026-1434-baseline-135m`](runs/10-17-2026-1434-baseline-135m) | `v0.1.1` | smollm2-135m | bf16 | 14.9 / 10.5 | 8078 (llama.cpp) / 155 (mlx) | x543 / x15 |
| [`10-17-2026-1434-baseline-135m`](runs/10-17-2026-1434-baseline-135m) | `v0.1.1` | smollm2-135m | q4 | 18.7 / 12.1 | 7842 (llama.cpp) / 408 (mlx) | x419 / x34 |
| [`10-17-2026-1511-baseline-360m`](runs/10-17-2026-1511-baseline-360m) | `v0.1.1` | smollm2-360m-instruct | bf16 | 11.2 / 8.4 | 3675 (llama.cpp) / 101 (llama.cpp) | x329 / x12 |
| [`10-17-2026-1511-baseline-360m`](runs/10-17-2026-1511-baseline-360m) | `v0.1.1` | smollm2-360m-instruct | q4 | 15.7 / 10.6 | 3738 (llama.cpp) / 256 (mlx) | x239 / x24 |
| [`10-31-2026-1705-llama-3.2-1b-baseline-v2`](runs/10-31-2026-1705-llama-3.2-1b-baseline-v2) | `v0.1.1-63-g566f6dd` | Llama-3.2-1B | bf16 | 18.2 / 15.8 | 1415 (llama.cpp) / 40 (llama.cpp) | x78 / x2 |
| [`10-31-2026-1705-llama-3.2-1b-baseline-v2`](runs/10-31-2026-1705-llama-3.2-1b-baseline-v2) | `v0.1.1-63-g566f6dd` | Llama-3.2-1B | q4 | 32.3 / 22.7 | 1468 (llama.cpp) / 113 (llama.cpp) | x45 / x5 |
| [`10-31-2026-1905-decode-occupancy-v1`](runs/10-31-2026-1905-decode-occupancy-v1) | `v0.1.1-78-gfc9d700` | Llama-3.2-1B | bf16 | 73.6 / 28.3 | 1420 (llama.cpp) / 42 (llama.cpp) | x19 / x1 |
| [`10-31-2026-1905-decode-occupancy-v1`](runs/10-31-2026-1905-decode-occupancy-v1) | `v0.1.1-78-gfc9d700` | Llama-3.2-1B | q4 | 59.7 / 41.6 | 1463 (llama.cpp) / 115 (llama.cpp) | x24 / x3 |
| [`10-31-2026-1905-decode-occupancy-v1`](runs/10-31-2026-1905-decode-occupancy-v1) | `v0.1.1-78-gfc9d700` | smollm2-135m | bf16 | 380.0 / 43.0 | 7874 (llama.cpp) / 226 (mlx) | x21 / x5 |
| [`10-31-2026-1905-decode-occupancy-v1`](runs/10-31-2026-1905-decode-occupancy-v1) | `v0.1.1-78-gfc9d700` | smollm2-135m | q4 | 116.5 / 45.4 | 8382 (llama.cpp) / 417 (mlx) | x72 / x9 |
| [`10-31-2026-1905-decode-occupancy-v1`](runs/10-31-2026-1905-decode-occupancy-v1) | `v0.1.1-78-gfc9d700` | smollm2-360m-instruct | bf16 | 143.0 / 34.5 | 3662 (llama.cpp) / 117 (llama.cpp) | x26 / x3 |
| [`10-31-2026-1905-decode-occupancy-v1`](runs/10-31-2026-1905-decode-occupancy-v1) | `v0.1.1-78-gfc9d700` | smollm2-360m-instruct | q4 | 90.3 / 39.4 | 3711 (llama.cpp) / 255 (mlx) | x41 / x6 |

gap = best engine / bare.metal (x1000 means the best engine is 1000x faster).
Quant rows compare different quantization schemes, so token match is informational.

## Progress (bare.metal, bf16)

| run | model | prefill tok/s | decode tok/s | J/token | gap pre | gap dec |
|---|---|---:|---:|---:|---:|---:|
| `10-17-2026-1434-baseline-135m` | smollm2-135m | 14.9 | 10.5 | 0.100 | x543 | x15 |
| `10-17-2026-1511-baseline-360m` | smollm2-360m-instruct | 11.2 | 8.4 | 0.144 | x329 | x12 |
| `10-31-2026-1705-llama-3.2-1b-baseline-v2` | Llama-3.2-1B | 18.2 | 15.8 | 0.680 | x78 | x2 |
| `10-31-2026-1905-decode-occupancy-v1` | Llama-3.2-1B | 73.6 | 28.3 | 0.388 | x19 | x1 |
| `10-31-2026-1905-decode-occupancy-v1` | smollm2-135m | 380.0 | 43.0 | 0.090 | x21 | x5 |
| `10-31-2026-1905-decode-occupancy-v1` | smollm2-360m-instruct | 143.0 | 34.5 | 0.173 | x26 | x3 |

## Run details

<details><summary><code>10-17-2026-1434-baseline-135m</code> &mdash; v0.1.1 &mdash; smollm2-135m</summary>

config: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=prep,cross,sweep,aggregate`

#### smollm2-135m &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 14.9 | 8,077.7 | 4,047.7 | 3,350.7 |
| decode tok/s | 10.5 | 153.5 | 155.2 | 84.0 |
| TTFT ms | 5,916 | 11 | 22 | 27 |
| ITL ms | 94.4 | 6.5 | 6.1 | 10.6 |
| peak RSS MB | 1,123 | 397 | 705 | 504 |
| peak GPU MB | 648 | - | 340 | 1,154 |
| J/token | 0.100 | 0.083 | 0.051 | 0.106 |
| token match % | 100.0 | 100.0 | 28.1 | 30.5 |

#### smollm2-135m &middot; q4

| metric | bare.metal | llama.cpp | mlx |
|---|---:|---:|---:|
| prefill tok/s | 18.7 | 7,842.4 | 7,016.2 |
| decode tok/s | 12.1 | 255.8 | 408.2 |
| TTFT ms | 4,703 | 11 | 13 |
| ITL ms | 82.3 | 3.9 | 2.4 |
| peak RSS MB | 973 | 217 | 514 |
| peak GPU MB | 502 | - | 198 |
| J/token | 0.070 | 0.063 | 0.069 |
| token match % | 6.2 | 6.2 | 6.2 |

#### smollm2-135m &middot; bare.metal context sweep

| config | prompt | prefill tok/s | decode tok/s | TTFT ms | ITL ms |
|---|---:|---:|---:|---:|---:|
| `p128_bf16` | 128 | 13.6 | 9.4 | 9393 | 106.6 |
| `p128_fp16` | 128 | 13.7 | 9.3 | 9371 | 107.4 |
| `p128_q4` | 128 | 16.9 | 10.7 | 7571 | 92.5 |
| `p128_q8` | 128 | 16.7 | 10.7 | 7660 | 93.2 |
| `p512_bf16` | 512 | 8.1 | 4.8 | 62883 | 207.4 |
| `p1024_bf16` | 1024 | 5.8 | 5.4 | 175245 | 183.3 |

</details>

<details><summary><code>10-17-2026-1511-baseline-360m</code> &mdash; v0.1.1 &mdash; smollm2-360m-instruct</summary>

config: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=prep,cross,sweep,aggregate`

#### smollm2-360m-instruct &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 11.2 | 3,674.9 | 2,690.9 | 1,341.4 |
| decode tok/s | 8.4 | 100.7 | 97.2 | 46.8 |
| TTFT ms | 7,886 | 24 | 33 | 66 |
| ITL ms | 118.7 | 9.9 | 10.7 | 21.2 |
| peak RSS MB | 2,924 | 862 | 1,160 | 511 |
| peak GPU MB | 1,397 | - | 835 | 1,152 |
| J/token | 0.144 | 0.192 | 0.105 | 0.143 |
| token match % | 100.0 | 100.0 | 19.5 | 19.5 |

#### smollm2-360m-instruct &middot; q4

| metric | bare.metal | llama.cpp | mlx |
|---|---:|---:|---:|
| prefill tok/s | 15.7 | 3,737.9 | 3,355.2 |
| decode tok/s | 10.6 | 150.4 | 256.4 |
| TTFT ms | 5,617 | 24 | 26 |
| ITL ms | 94.9 | 6.6 | 3.9 |
| peak RSS MB | 2,508 | 366 | 644 |
| peak GPU MB | 965 | - | 349 |
| J/token | 0.095 | 0.097 | 0.123 |
| token match % | 1.6 | 1.6 | 1.6 |

#### smollm2-360m-instruct &middot; bare.metal context sweep

| config | prompt | prefill tok/s | decode tok/s | TTFT ms | ITL ms |
|---|---:|---:|---:|---:|---:|
| `p128_bf16` | 128 | 10.5 | 7.7 | 12140 | 129.7 |
| `p128_fp16` | 128 | 10.5 | 7.7 | 12211 | 130.1 |
| `p128_q4` | 128 | 14.4 | 9.5 | 8905 | 105.1 |
| `p128_q8` | 128 | 14.0 | 9.4 | 9137 | 107.2 |
| `p512_bf16` | 512 | 6.8 | 4.2 | 75569 | 235.7 |
| `p1024_bf16` | 1024 | 5.3 | 5.1 | 193765 | 198.0 |

</details>

<details><summary><code>10-31-2026-1705-llama-3.2-1b-baseline-v2</code> &mdash; v0.1.1-63-g566f6dd &mdash; Llama-3.2-1B</summary>

config: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=cross,aggregate`

#### Llama-3.2-1B &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 18.2 | 1,415.3 | 1,022.9 | 848.3 |
| decode tok/s | 15.8 | 39.6 | 34.1 | 33.0 |
| TTFT ms | 4,893 | 63 | 87 | 105 |
| ITL ms | 63.3 | 25.3 | 29.0 | 30.3 |
| peak RSS MB | 7,427 | 2,660 | 2,898 | 595 |
| peak GPU MB | 2,609 | - | 2,588 | 3,283 |
| J/token | 0.680 | 1.200 | 0.649 | 0.596 |
| token match % | 100.0 | 100.0 | 1.6 | 100.0 |

#### Llama-3.2-1B &middot; q4

| metric | bare.metal | llama.cpp | mlx |
|---|---:|---:|---:|
| prefill tok/s | 32.3 | 1,467.8 | 1,001.5 |
| decode tok/s | 22.7 | 112.6 | 93.6 |
| TTFT ms | 2,757 | 61 | 89 |
| ITL ms | 40.2 | 8.9 | 10.6 |
| peak RSS MB | 5,881 | 954 | 1,462 |
| peak GPU MB | 1,271 | - | 877 |
| J/token | 0.384 | 0.467 | 0.155 |
| token match % | 2.3 | 2.3 | 2.3 |

</details>

<details><summary><code>10-31-2026-1905-decode-occupancy-v1</code> &mdash; v0.1.1-78-gfc9d700 &mdash; Llama-3.2-1B, smollm2-135m, smollm2-360m-instruct</summary>

config: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=prep,cross,sweep,aggregate`

#### Llama-3.2-1B &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 73.6 | 1,420.0 | 1,010.4 | 853.8 |
| decode tok/s | 28.3 | 41.5 | 35.0 | 34.6 |
| TTFT ms | 1,210 | 63 | 88 | 104 |
| ITL ms | 35.3 | 24.1 | 28.5 | 28.7 |
| peak RSS MB | 6,056 | 2,661 | 3,239 | 595 |
| peak GPU MB | 2,985 | - | 2,588 | 3,274 |
| J/token | 0.388 | 0.934 | 0.395 | 0.475 |
| token match % | 100.0 | 100.0 | 1.6 | 100.0 |

#### Llama-3.2-1B &middot; q4

| metric | bare.metal | llama.cpp | mlx |
|---|---:|---:|---:|
| prefill tok/s | 59.7 | 1,462.6 | 1,124.6 |
| decode tok/s | 41.6 | 115.2 | 94.9 |
| TTFT ms | 1,490 | 61 | 79 |
| ITL ms | 24.0 | 8.7 | 10.3 |
| peak RSS MB | 7,427 | 953 | 1,463 |
| peak GPU MB | 1,271 | - | 877 |
| J/token | 0.283 | 0.430 | 0.128 |
| token match % | 2.3 | 2.3 | 2.3 |

#### Llama-3.2-1B &middot; bare.metal context sweep

| config | prompt | prefill tok/s | decode tok/s | TTFT ms | ITL ms |
|---|---:|---:|---:|---:|---:|
| `p128_bf16` | 128 | 73.6 | 26.1 | 1738 | 38.3 |
| `p128_fp16` | 128 | 73.6 | 26.2 | 1740 | 38.3 |
| `p128_q4` | 128 | 55.5 | 37.3 | 2307 | 26.8 |
| `p128_q8` | 128 | 46.3 | 32.9 | 2767 | 30.2 |
| `p512_bf16` | 512 | 73.6 | 15.8 | 6952 | 63.3 |
| `p1024_bf16` | 1024 | 72.2 | 10.3 | 14176 | 97.3 |

#### smollm2-135m &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 380.0 | 7,874.2 | 6,656.0 | 4,088.5 |
| decode tok/s | 43.0 | 153.1 | 225.8 | 101.1 |
| TTFT ms | 232 | 11 | 13 | 22 |
| ITL ms | 23.1 | 6.5 | 4.4 | 9.9 |
| peak RSS MB | 873 | 402 | 705 | 505 |
| peak GPU MB | 562 | - | 340 | 1,154 |
| J/token | 0.090 | 0.097 | 0.086 | 0.122 |
| token match % | 100.0 | 100.0 | 28.1 | 30.5 |

#### smollm2-135m &middot; q4

| metric | bare.metal | llama.cpp | mlx |
|---|---:|---:|---:|
| prefill tok/s | 116.5 | 8,381.7 | 7,070.2 |
| decode tok/s | 45.4 | 222.2 | 417.0 |
| TTFT ms | 756 | 10 | 12 |
| ITL ms | 22.0 | 4.5 | 2.4 |
| peak RSS MB | 820 | 224 | 515 |
| peak GPU MB | 219 | - | 198 |
| J/token | 0.090 | 0.053 | 0.072 |
| token match % | 6.2 | 6.2 | 6.2 |

#### smollm2-135m &middot; bare.metal context sweep

| config | prompt | prefill tok/s | decode tok/s | TTFT ms | ITL ms |
|---|---:|---:|---:|---:|---:|
| `p128_bf16` | 128 | 394.3 | 35.2 | 325 | 28.2 |
| `p128_fp16` | 128 | 395.4 | 35.0 | 324 | 28.5 |
| `p128_q4` | 128 | 90.3 | 37.1 | 1418 | 27.0 |
| `p128_q8` | 128 | 89.2 | 36.9 | 1434 | 27.1 |
| `p512_bf16` | 512 | 412.0 | 13.2 | 1243 | 75.9 |
| `p1024_bf16` | 1024 | 396.0 | 7.2 | 2586 | 139.4 |

#### smollm2-360m-instruct &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 143.0 | 3,662.3 | 1,934.8 | 2,084.4 |
| decode tok/s | 34.5 | 116.9 | 83.5 | 62.6 |
| TTFT ms | 615 | 24 | 45 | 42 |
| ITL ms | 28.9 | 8.6 | 12.3 | 15.9 |
| peak RSS MB | 2,260 | 867 | 1,160 | 506 |
| peak GPU MB | 1,243 | - | 835 | 1,160 |
| J/token | 0.173 | 0.325 | 0.083 | 0.204 |
| token match % | 100.0 | 100.0 | 19.5 | 19.5 |

#### smollm2-360m-instruct &middot; q4

| metric | bare.metal | llama.cpp | mlx |
|---|---:|---:|---:|
| prefill tok/s | 90.3 | 3,711.0 | 3,383.9 |
| decode tok/s | 39.4 | 147.6 | 255.2 |
| TTFT ms | 975 | 24 | 26 |
| ITL ms | 25.4 | 6.8 | 3.9 |
| peak RSS MB | 2,183 | 371 | 644 |
| peak GPU MB | 461 | - | 349 |
| J/token | 0.146 | 0.101 | 0.133 |
| token match % | 1.6 | 1.6 | 1.6 |

#### smollm2-360m-instruct &middot; bare.metal context sweep

| config | prompt | prefill tok/s | decode tok/s | TTFT ms | ITL ms |
|---|---:|---:|---:|---:|---:|
| `p128_bf16` | 128 | 145.0 | 29.1 | 883 | 34.4 |
| `p128_fp16` | 128 | 145.0 | 29.0 | 883 | 34.5 |
| `p128_q4` | 128 | 72.8 | 32.6 | 1759 | 30.7 |
| `p128_q8` | 128 | 69.3 | 31.8 | 1847 | 31.4 |
| `p512_bf16` | 512 | 145.2 | 11.7 | 3527 | 84.9 |
| `p1024_bf16` | 1024 | 138.4 | 6.5 | 7401 | 152.5 |

</details>

_Auto-generated by `tools/index.py` - do not edit by hand._
