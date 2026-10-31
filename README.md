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
| [`10-31-2026-2235-mmap-weights-v1`](runs/10-31-2026-2235-mmap-weights-v1) | `v0.1.1-101-g2eb12f3` | Llama-3.2-1B | bf16 | 70.4 / 27.3 | 1391 (llama.cpp) / 40 (llama.cpp) | x20 / x1 |
| [`10-31-2026-2235-mmap-weights-v1`](runs/10-31-2026-2235-mmap-weights-v1) | `v0.1.1-101-g2eb12f3` | Llama-3.2-1B | q4 | 57.2 / 40.5 | 1419 (llama.cpp) / 109 (llama.cpp) | x25 / x3 |
| [`10-31-2026-2235-mmap-weights-v1`](runs/10-31-2026-2235-mmap-weights-v1) | `v0.1.1-101-g2eb12f3` | smollm2-135m | bf16 | 355.1 / 42.5 | 6812 (mlx) / 203 (mlx) | x19 / x5 |
| [`10-31-2026-2235-mmap-weights-v1`](runs/10-31-2026-2235-mmap-weights-v1) | `v0.1.1-101-g2eb12f3` | smollm2-135m | q4 | 112.6 / 44.8 | 7955 (llama.cpp) / 359 (mlx) | x71 / x8 |
| [`10-31-2026-2235-mmap-weights-v1`](runs/10-31-2026-2235-mmap-weights-v1) | `v0.1.1-101-g2eb12f3` | smollm2-360m-instruct | bf16 | 136.3 / 33.7 | 3657 (llama.cpp) / 108 (llama.cpp) | x27 / x3 |
| [`10-31-2026-2235-mmap-weights-v1`](runs/10-31-2026-2235-mmap-weights-v1) | `v0.1.1-101-g2eb12f3` | smollm2-360m-instruct | q4 | 86.7 / 38.7 | 3657 (llama.cpp) / 230 (mlx) | x42 / x6 |

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
| `10-31-2026-2235-mmap-weights-v1` | Llama-3.2-1B | 70.4 | 27.3 | 0.409 | x20 | x1 |
| `10-31-2026-2235-mmap-weights-v1` | smollm2-135m | 355.1 | 42.5 | 0.098 | x19 | x5 |
| `10-31-2026-2235-mmap-weights-v1` | smollm2-360m-instruct | 136.3 | 33.7 | 0.206 | x27 | x3 |

## Training (bare.metal)

| run | model | prec | B | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | J/token | parity |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `10-31-2026-2154-train-baseline-v1` | smollm2-135m | bf16 | 1 | 64 | 20 | 598.9 | 105.6 | 2.2786 -> 2.6379 | 3105 | 2598 | 0.0694 | PASS (5.7e-07) |
| `10-31-2026-2154-train-baseline-v1` | smollm2-135m | bf16 | 4 | 64 | 20 | 2276.0 | 112.1 | 2.6485 -> 2.3935 | 3105 | 2598 | 0.0755 | PASS (3.6e-07) |
| `10-31-2026-2154-train-baseline-v1` | smollm2-135m | fp32 | 1 | 64 | 20 | 591.4 | 107.1 | 2.2786 -> 2.7159 | 2835 | 2329 | 0.0948 | PASS (1.0e-07) |
| `10-31-2026-2154-train-baseline-v1` | smollm2-135m | fp32 | 4 | 64 | 20 | 2247.6 | 113.3 | 2.6485 -> 2.4067 | 2836 | 2329 | 0.0794 | PASS (9.0e-08) |

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
| load ms | 606 | - | 250 | 500 |
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
| load ms | 199 | - | 157 |
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
| load ms | 1,578 | - | 447 | 493 |
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
| load ms | 498 | - | 212 |
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
| load ms | 4,105 | - | 1,465 | 2,620 |
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
| load ms | 6,476 | - | 858 |
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
| load ms | 6,557 | - | 1,712 | 2,558 |
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
| load ms | 2,111 | - | 864 |
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
| load ms | 557 | - | 250 | 272 |
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
| load ms | 198 | - | 159 |
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
| load ms | 1,465 | - | 432 | 370 |
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
| load ms | 494 | - | 217 |
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

<details><summary><code>10-31-2026-2154-train-baseline-v1</code> &mdash; v0.1.1-84-g2aba0ca &mdash; smollm2-135m</summary>

config: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=train,aggregate,train_steps=20,train_seq=64`

#### smollm2-135m &middot; bare.metal training

| cfg | prec | B | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | J/token | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `bf16_b1` | bf16 | 1 | 64 | 20 | 598.9 | 105.6 | 2.2786 -> 2.6379 | 3105 | 2598 | 0.0694 | PASS (5.7e-07) |
| `bf16_b4` | bf16 | 4 | 64 | 20 | 2276.0 | 112.1 | 2.6485 -> 2.3935 | 3105 | 2598 | 0.0755 | PASS (3.6e-07) |
| `fp32_b1` | fp32 | 1 | 64 | 20 | 591.4 | 107.1 | 2.2786 -> 2.7159 | 2835 | 2329 | 0.0948 | PASS (1.0e-07) |
| `fp32_b4` | fp32 | 4 | 64 | 20 | 2247.6 | 113.3 | 2.6485 -> 2.4067 | 2836 | 2329 | 0.0794 | PASS (9.0e-08) |

</details>

<details><summary><code>10-31-2026-2235-mmap-weights-v1</code> &mdash; v0.1.1-101-g2eb12f3 &mdash; Llama-3.2-1B, smollm2-135m, smollm2-360m-instruct</summary>

config: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=cross,aggregate,train_steps=20,train_seq=64`

#### Llama-3.2-1B &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 70.4 | 1,390.9 | 1,004.3 | 840.3 |
| decode tok/s | 27.3 | 39.8 | 34.4 | 32.4 |
| TTFT ms | 1,265 | 64 | 89 | 106 |
| ITL ms | 36.4 | 25.1 | 28.9 | 30.3 |
| peak RSS MB | 4,692 | 2,664 | 1,504 | 595 |
| peak GPU MB | 2,985 | - | 2,588 | 3,283 |
| load ms | 4,315 | - | 1,821 | 2,790 |
| J/token | 0.409 | 1.014 | 0.517 | 0.576 |
| token match % | 100.0 | 100.0 | 1.6 | 100.0 |

#### Llama-3.2-1B &middot; q4

| metric | bare.metal | llama.cpp | mlx |
|---|---:|---:|---:|
| prefill tok/s | 57.2 | 1,418.8 | 1,160.6 |
| decode tok/s | 40.5 | 108.7 | 95.3 |
| TTFT ms | 1,558 | 63 | 77 |
| ITL ms | 25.1 | 9.2 | 10.3 |
| peak RSS MB | 4,149 | 953 | 1,463 |
| peak GPU MB | 1,271 | - | 880 |
| load ms | 4,858 | - | 919 |
| J/token | 0.306 | 0.492 | 0.191 |
| token match % | 2.3 | 2.3 | 2.3 |

#### smollm2-135m &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 355.1 | 6,661.2 | 6,812.4 | 4,065.8 |
| decode tok/s | 42.5 | 182.8 | 202.8 | 85.9 |
| TTFT ms | 248 | 13 | 13 | 22 |
| ITL ms | 23.5 | 5.5 | 4.5 | 10.7 |
| peak RSS MB | 615 | 405 | 705 | 505 |
| peak GPU MB | 562 | - | 340 | 1,154 |
| load ms | 477 | - | 253 | 349 |
| J/token | 0.098 | 0.145 | 0.119 | 0.138 |
| token match % | 100.0 | 100.0 | 28.1 | 30.5 |

#### smollm2-135m &middot; q4

| metric | bare.metal | llama.cpp | mlx |
|---|---:|---:|---:|
| prefill tok/s | 112.6 | 7,954.8 | 7,068.6 |
| decode tok/s | 44.8 | 227.1 | 358.8 |
| TTFT ms | 782 | 11 | 12 |
| ITL ms | 22.3 | 4.4 | 2.4 |
| peak RSS MB | 470 | 226 | 515 |
| peak GPU MB | 219 | - | 198 |
| load ms | 287 | - | 159 |
| J/token | 0.102 | 0.064 | 0.072 |
| token match % | 6.2 | 6.2 | 6.2 |

#### smollm2-360m-instruct &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 136.3 | 3,656.6 | 2,969.6 | 1,944.5 |
| decode tok/s | 33.7 | 108.2 | 83.0 | 60.6 |
| TTFT ms | 645 | 24 | 30 | 46 |
| ITL ms | 29.6 | 9.2 | 11.9 | 16.5 |
| peak RSS MB | 1,563 | 866 | 1,159 | 505 |
| peak GPU MB | 1,243 | - | 835 | 1,160 |
| load ms | 1,326 | - | 443 | 949 |
| J/token | 0.206 | 0.404 | 0.168 | 0.309 |
| token match % | 100.0 | 100.0 | 19.5 | 19.5 |

#### smollm2-360m-instruct &middot; q4

| metric | bare.metal | llama.cpp | mlx |
|---|---:|---:|---:|
| prefill tok/s | 86.7 | 3,657.5 | 3,351.0 |
| decode tok/s | 38.7 | 169.1 | 229.9 |
| TTFT ms | 1,015 | 24 | 26 |
| ITL ms | 25.7 | 5.9 | 4.0 |
| peak RSS MB | 1,131 | 372 | 642 |
| peak GPU MB | 461 | - | 349 |
| load ms | 455 | - | 219 |
| J/token | 0.160 | 0.130 | 0.141 |
| token match % | 1.6 | 1.6 | 1.6 |

</details>

_Auto-generated by `tools/index.py` - do not edit by hand._
