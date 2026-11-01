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
| [`10-31-2026-2245-mmap-weights-8192`](runs/10-31-2026-2245-mmap-weights-8192) | `v0.1.1-101-g2eb12f3` | smollm2-135m | bf16 | 346.9 / 42.5 | 7834 (llama.cpp) / 178 (llama.cpp) | x23 / x4 |
| [`10-31-2026-2313-quant-prefill-v1`](runs/10-31-2026-2313-quant-prefill-v1) | `v0.1.1-106-g23dc1ba` | Llama-3.2-1B | bf16 | 72.8 / 27.8 | 1418 (llama.cpp) / 41 (llama.cpp) | x19 / x1 |
| [`10-31-2026-2313-quant-prefill-v1`](runs/10-31-2026-2313-quant-prefill-v1) | `v0.1.1-106-g23dc1ba` | Llama-3.2-1B | q4 | 148.5 / 41.5 | 1463 (llama.cpp) / 111 (llama.cpp) | x10 / x3 |
| [`10-31-2026-2313-quant-prefill-v1`](runs/10-31-2026-2313-quant-prefill-v1) | `v0.1.1-106-g23dc1ba` | smollm2-135m | bf16 | 383.1 / 43.2 | 7433 (llama.cpp) / 197 (mlx) | x19 / x5 |
| [`10-31-2026-2313-quant-prefill-v1`](runs/10-31-2026-2313-quant-prefill-v1) | `v0.1.1-106-g23dc1ba` | smollm2-135m | q4 | 824.3 / 45.2 | 7866 (llama.cpp) / 409 (mlx) | x10 / x9 |
| [`10-31-2026-2313-quant-prefill-v1`](runs/10-31-2026-2313-quant-prefill-v1) | `v0.1.1-106-g23dc1ba` | smollm2-360m-instruct | bf16 | 142.9 / 34.4 | 3717 (llama.cpp) / 100 (llama.cpp) | x26 / x3 |
| [`10-31-2026-2313-quant-prefill-v1`](runs/10-31-2026-2313-quant-prefill-v1) | `v0.1.1-106-g23dc1ba` | smollm2-360m-instruct | q4 | 379.1 / 39.1 | 3680 (llama.cpp) / 247 (mlx) | x10 / x6 |
| [`10-31-2026-2350-prefill-gemm-v1`](runs/10-31-2026-2350-prefill-gemm-v1) | `v0.1.1-106-g16fcf7d` | Llama-3.2-1B | bf16 | 221.5 / 28.2 | 1408 (llama.cpp) / 41 (llama.cpp) | x6 / x1 |
| [`10-31-2026-2350-prefill-gemm-v1`](runs/10-31-2026-2350-prefill-gemm-v1) | `v0.1.1-106-g16fcf7d` | smollm2-135m | bf16 | 972.2 / 43.3 | 8243 (llama.cpp) / 231 (mlx) | x8 / x5 |
| [`10-31-2026-2350-prefill-gemm-v1`](runs/10-31-2026-2350-prefill-gemm-v1) | `v0.1.1-106-g16fcf7d` | smollm2-360m-instruct | bf16 | 510.7 / 34.6 | 3712 (llama.cpp) / 113 (llama.cpp) | x7 / x3 |

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
| `10-31-2026-2245-mmap-weights-8192` | smollm2-135m | 346.9 | 42.5 | 0.098 | x23 | x4 |
| `10-31-2026-2313-quant-prefill-v1` | Llama-3.2-1B | 72.8 | 27.8 | 0.407 | x19 | x1 |
| `10-31-2026-2313-quant-prefill-v1` | smollm2-135m | 383.1 | 43.2 | 0.103 | x19 | x5 |
| `10-31-2026-2313-quant-prefill-v1` | smollm2-360m-instruct | 142.9 | 34.4 | 0.236 | x26 | x3 |
| `10-31-2026-2350-prefill-gemm-v1` | Llama-3.2-1B | 221.5 | 28.2 | 0.299 | x6 | x1 |
| `10-31-2026-2350-prefill-gemm-v1` | smollm2-135m | 972.2 | 43.3 | 0.083 | x8 | x5 |
| `10-31-2026-2350-prefill-gemm-v1` | smollm2-360m-instruct | 510.7 | 34.6 | 0.145 | x7 | x3 |

## Training (bare.metal)

| run | model | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | J/token | parity |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `10-31-2026-2154-train-baseline-v1` | smollm2-135m | bf16 | 1 | 1 | 64 | 20 | 598.9 | 105.6 | 2.2786 -> 2.6379 | 3105 | 2598 | 0.0694 | PASS (5.7e-07) |
| `10-31-2026-2154-train-baseline-v1` | smollm2-135m | bf16 | 4 | 1 | 64 | 20 | 2276.0 | 112.1 | 2.6485 -> 2.3935 | 3105 | 2598 | 0.0755 | PASS (3.6e-07) |
| `10-31-2026-2154-train-baseline-v1` | smollm2-135m | fp32 | 1 | 1 | 64 | 20 | 591.4 | 107.1 | 2.2786 -> 2.7159 | 2835 | 2329 | 0.0948 | PASS (1.0e-07) |
| `10-31-2026-2154-train-baseline-v1` | smollm2-135m | fp32 | 4 | 1 | 64 | 20 | 2247.6 | 113.3 | 2.6485 -> 2.4067 | 2836 | 2329 | 0.0794 | PASS (9.0e-08) |
| `11-01-2026-0006-train-grad-accum-v1` | smollm2-135m | bf16 | 1 | 1 | 64 | 20 | 596.5 | 106.0 | 2.2786 -> 2.6379 | 3105 | 2598 | 0.0726 | PASS (1.1e-06) |
| `11-01-2026-0006-train-grad-accum-v1` | smollm2-135m | bf16 | 4 | 1 | 64 | 20 | 2266.7 | 112.4 | 2.6485 -> 2.3935 | 3107 | 2598 | 0.0689 | PASS (8.9e-07) |
| `11-01-2026-0006-train-grad-accum-v1` | smollm2-135m | bf16 | 1 | 4 | 64 | 20 | 542.6 | 112.3 | 2.2786 -> 2.9371 | 3105 | 2598 | 0.0685 | PASS (0.0e+00) |
| `11-01-2026-0006-train-grad-accum-v1` | smollm2-135m | fp32 | 1 | 1 | 64 | 20 | 592.5 | 106.8 | 2.2786 -> 2.7159 | 2835 | 2329 | 0.0723 | PASS (7.8e-07) |
| `11-01-2026-0006-train-grad-accum-v1` | smollm2-135m | fp32 | 4 | 1 | 64 | 20 | 2246.9 | 113.8 | 2.6485 -> 2.4067 | 2836 | 2329 | 0.0719 | PASS (1.8e-07) |
| `11-01-2026-0006-train-grad-accum-v1` | smollm2-135m | fp32 | 1 | 4 | 64 | 20 | 551.8 | 113.3 | 2.2786 -> 2.9132 | 2835 | 2329 | 0.0703 | PASS (0.0e+00) |
| `11-01-2026-1255-train-occupancy-v1` | smollm2-135m | bf16 | 1 | 1 | 64 | 20 | 384.1 | 163.3 | 2.2786 -> 2.6379 | 3087 | 2598 | - | PASS (9.5e-08) |
| `11-01-2026-1255-train-occupancy-v1` | smollm2-135m | bf16 | 4 | 1 | 64 | 20 | 1407.1 | 181.8 | 2.6485 -> 2.3935 | 3088 | 2598 | - | PASS (1.8e-07) |
| `11-01-2026-1255-train-occupancy-v1` | smollm2-135m | bf16 | 1 | 4 | 64 | 20 | 330.3 | 184.8 | 2.2786 -> 2.9371 | 3087 | 2598 | - | PASS (0.0e+00) |
| `11-01-2026-1255-train-occupancy-v1` | smollm2-135m | fp32 | 1 | 1 | 64 | 20 | 372.9 | 171.0 | 2.2786 -> 2.7159 | 2817 | 2329 | - | PASS (2.6e-07) |
| `11-01-2026-1255-train-occupancy-v1` | smollm2-135m | fp32 | 4 | 1 | 64 | 20 | 1366.0 | 187.3 | 2.6485 -> 2.4067 | 2818 | 2329 | - | PASS (2.7e-07) |
| `11-01-2026-1255-train-occupancy-v1` | smollm2-135m | fp32 | 1 | 4 | 64 | 20 | 332.0 | 187.4 | 2.2786 -> 2.9132 | 2817 | 2329 | - | PASS (0.0e+00) |
| `11-01-2026-1414-train-grad-accum-fix-v1` | smollm2-135m | bf16 | 1 | 1 | 64 | 20 | 381.0 | 166.5 | 2.2786 -> 2.6379 | 3087 | 2598 | - | PASS (2.6e-07) |
| `11-01-2026-1414-train-grad-accum-fix-v1` | smollm2-135m | bf16 | 4 | 1 | 64 | 20 | 1408.9 | 182.5 | 2.6485 -> 2.3556 | 3088 | 2598 | - | PASS (5.4e-07) |
| `11-01-2026-1414-train-grad-accum-fix-v1` | smollm2-135m | bf16 | 1 | 4 | 64 | 20 | 328.7 | 184.2 | 2.2786 -> 2.9272 | 3087 | 2598 | - | PASS (0.0e+00) |
| `11-01-2026-1414-train-grad-accum-fix-v1` | smollm2-135m | fp32 | 1 | 1 | 64 | 20 | 371.5 | 170.9 | 2.2786 -> 2.7159 | 2817 | 2329 | - | PASS (4.4e-07) |
| `11-01-2026-1414-train-grad-accum-fix-v1` | smollm2-135m | fp32 | 4 | 1 | 64 | 20 | 1362.6 | 187.8 | 2.6485 -> 2.3772 | 2818 | 2329 | - | PASS (4.5e-07) |
| `11-01-2026-1414-train-grad-accum-fix-v1` | smollm2-135m | fp32 | 1 | 4 | 64 | 20 | 330.6 | 188.3 | 2.2786 -> 2.9035 | 2817 | 2329 | - | PASS (0.0e+00) |

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

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | J/token | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `bf16_b1` | bf16 | 1 | 1 | 64 | 20 | 598.9 | 105.6 | 2.2786 -> 2.6379 | 3105 | 2598 | 0.0694 | PASS (5.7e-07) |
| `bf16_b4` | bf16 | 4 | 1 | 64 | 20 | 2276.0 | 112.1 | 2.6485 -> 2.3935 | 3105 | 2598 | 0.0755 | PASS (3.6e-07) |
| `fp32_b1` | fp32 | 1 | 1 | 64 | 20 | 591.4 | 107.1 | 2.2786 -> 2.7159 | 2835 | 2329 | 0.0948 | PASS (1.0e-07) |
| `fp32_b4` | fp32 | 4 | 1 | 64 | 20 | 2247.6 | 113.3 | 2.6485 -> 2.4067 | 2836 | 2329 | 0.0794 | PASS (9.0e-08) |

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

<details><summary><code>10-31-2026-2245-mmap-weights-8192</code> &mdash; v0.1.1-101-g2eb12f3 &mdash; smollm2-135m</summary>

config: `prompt_cap=128,gen=128,reps=3,formats=bf16,stages=cross,aggregate,train_steps=20,train_seq=64`

#### smollm2-135m &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 346.9 | 7,834.3 | 4,874.0 | 3,948.8 |
| decode tok/s | 42.5 | 178.2 | 117.2 | 92.9 |
| TTFT ms | 254 | 11 | 18 | 23 |
| ITL ms | 23.5 | 5.6 | 8.1 | 10.4 |
| peak RSS MB | 615 | 403 | 705 | 504 |
| peak GPU MB | 1,128 | - | 340 | 1,154 |
| load ms | 471 | - | 238 | 357 |
| J/token | 0.098 | 0.137 | 0.057 | 0.131 |
| token match % | 100.0 | 100.0 | 28.1 | 30.5 |

</details>

<details><summary><code>10-31-2026-2313-quant-prefill-v1</code> &mdash; v0.1.1-106-g23dc1ba &mdash; Llama-3.2-1B, smollm2-135m, smollm2-360m-instruct</summary>

config: `prompt_cap=128,gen=128,reps=3,formats=bf16,q4,q8,stages=cross,sweep,aggregate,train_steps=20,train_seq=64`

#### Llama-3.2-1B &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 72.8 | 1,417.6 | 1,032.2 | 849.9 |
| decode tok/s | 27.8 | 41.2 | 34.8 | 33.9 |
| TTFT ms | 1,223 | 63 | 86 | 105 |
| ITL ms | 36.1 | 24.3 | 28.6 | 29.2 |
| peak RSS MB | 3,460 | 2,662 | 1,157 | 595 |
| peak GPU MB | 2,851 | - | 2,588 | 3,283 |
| load ms | 4,595 | - | 1,743 | 2,795 |
| J/token | 0.407 | 0.922 | 0.454 | 0.541 |
| token match % | 100.0 | 100.0 | 1.6 | 100.0 |

#### Llama-3.2-1B &middot; q4

| metric | bare.metal | llama.cpp | mlx |
|---|---:|---:|---:|
| prefill tok/s | 148.5 | 1,463.4 | 1,157.1 |
| decode tok/s | 41.5 | 110.9 | 100.1 |
| TTFT ms | 600 | 61 | 77 |
| ITL ms | 24.1 | 9.0 | 9.9 |
| peak RSS MB | 4,149 | 953 | 1,464 |
| peak GPU MB | 1,513 | - | 877 |
| load ms | 3,643 | - | 917 |
| J/token | 0.233 | 0.441 | 0.167 |
| token match % | 2.3 | 2.3 | 2.3 |

#### Llama-3.2-1B &middot; bare.metal context sweep

| config | prompt | prefill tok/s | decode tok/s | TTFT ms | ITL ms |
|---|---:|---:|---:|---:|---:|
| `p128_bf16` | 128 | 73.0 | 26.2 | 1753 | 38.1 |
| `p128_fp16` | 128 | 73.1 | 26.4 | 1751 | 37.9 |
| `p128_q4` | 128 | 149.7 | 37.5 | 855 | 26.7 |
| `p128_q8` | 128 | 178.6 | 33.1 | 717 | 30.2 |
| `p512_bf16` | 512 | 72.7 | 15.8 | 7040 | 63.5 |
| `p512_q4` | 512 | 145.8 | 19.2 | 3512 | 51.9 |
| `p512_q8` | 512 | 172.1 | 17.9 | 2975 | 55.8 |
| `p1024_bf16` | 1024 | 70.7 | 10.2 | 14483 | 97.6 |
| `p1024_q4` | 1024 | 137.3 | 11.6 | 7457 | 86.1 |
| `p1024_q8` | 1024 | 157.4 | 11.1 | 6504 | 89.9 |

#### smollm2-135m &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 383.1 | 7,433.5 | 6,649.9 | 4,113.5 |
| decode tok/s | 43.2 | 171.0 | 196.8 | 99.5 |
| TTFT ms | 230 | 12 | 13 | 22 |
| ITL ms | 23.1 | 5.8 | 5.0 | 9.9 |
| peak RSS MB | 615 | 402 | 705 | 505 |
| peak GPU MB | 468 | - | 340 | 1,154 |
| load ms | 532 | - | 252 | 313 |
| J/token | 0.103 | 0.112 | 0.060 | 0.131 |
| token match % | 100.0 | 100.0 | 28.1 | 30.5 |

#### smollm2-135m &middot; q4

| metric | bare.metal | llama.cpp | mlx |
|---|---:|---:|---:|
| prefill tok/s | 824.3 | 7,865.9 | 6,983.3 |
| decode tok/s | 45.2 | 245.8 | 408.6 |
| TTFT ms | 107 | 11 | 13 |
| ITL ms | 22.0 | 4.1 | 2.4 |
| peak RSS MB | 470 | 223 | 515 |
| peak GPU MB | 322 | - | 198 |
| load ms | 272 | - | 158 |
| J/token | 0.084 | 0.079 | 0.074 |
| token match % | 6.2 | 6.2 | 6.2 |

#### smollm2-135m &middot; bare.metal context sweep

| config | prompt | prefill tok/s | decode tok/s | TTFT ms | ITL ms |
|---|---:|---:|---:|---:|---:|
| `p128_bf16` | 128 | 393.7 | 35.4 | 325 | 28.3 |
| `p128_fp16` | 128 | 394.6 | 35.4 | 324 | 28.1 |
| `p128_q4` | 128 | 883.5 | 36.9 | 145 | 27.0 |
| `p128_q8` | 128 | 1001.2 | 36.4 | 128 | 27.3 |
| `p512_bf16` | 512 | 411.3 | 13.2 | 1245 | 75.9 |
| `p512_q4` | 512 | 958.4 | 13.4 | 534 | 74.7 |
| `p512_q8` | 512 | 1092.1 | 13.3 | 469 | 75.0 |
| `p1024_bf16` | 1024 | 394.2 | 7.2 | 2598 | 139.4 |
| `p1024_q4` | 1024 | 860.4 | 7.2 | 1190 | 138.2 |
| `p1024_q8` | 1024 | 996.7 | 7.2 | 1027 | 138.2 |

#### smollm2-360m-instruct &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 142.9 | 3,717.1 | 1,846.9 | 2,062.0 |
| decode tok/s | 34.4 | 100.3 | 83.7 | 62.3 |
| TTFT ms | 616 | 24 | 48 | 43 |
| ITL ms | 29.3 | 10.0 | 11.9 | 16.0 |
| peak RSS MB | 1,563 | 867 | 1,160 | 506 |
| peak GPU MB | 1,076 | - | 835 | 1,160 |
| load ms | 1,335 | - | 451 | 911 |
| J/token | 0.236 | 0.245 | 0.080 | 0.207 |
| token match % | 100.0 | 100.0 | 19.5 | 19.5 |

#### smollm2-360m-instruct &middot; q4

| metric | bare.metal | llama.cpp | mlx |
|---|---:|---:|---:|
| prefill tok/s | 379.1 | 3,680.0 | 3,392.7 |
| decode tok/s | 39.1 | 144.4 | 247.0 |
| TTFT ms | 232 | 24 | 26 |
| ITL ms | 25.6 | 6.9 | 4.0 |
| peak RSS MB | 1,131 | 370 | 644 |
| peak GPU MB | 643 | - | 349 |
| load ms | 413 | - | 217 |
| J/token | 0.121 | 0.103 | 0.152 |
| token match % | 1.6 | 1.6 | 1.6 |

#### smollm2-360m-instruct &middot; bare.metal context sweep

| config | prompt | prefill tok/s | decode tok/s | TTFT ms | ITL ms |
|---|---:|---:|---:|---:|---:|
| `p128_bf16` | 128 | 145.3 | 29.2 | 881 | 34.1 |
| `p128_fp16` | 128 | 145.6 | 29.2 | 879 | 34.0 |
| `p128_q4` | 128 | 391.7 | 32.5 | 327 | 30.7 |
| `p128_q8` | 128 | 433.8 | 31.6 | 295 | 31.5 |
| `p512_bf16` | 512 | 145.1 | 11.8 | 3529 | 84.7 |
| `p512_q4` | 512 | 393.4 | 12.2 | 1301 | 81.6 |
| `p512_q8` | 512 | 432.5 | 12.1 | 1184 | 82.2 |
| `p1024_bf16` | 1024 | 138.2 | 6.6 | 7410 | 152.6 |
| `p1024_q4` | 1024 | 342.3 | 6.7 | 2992 | 149.1 |
| `p1024_q8` | 1024 | 371.8 | 6.7 | 2754 | 149.9 |

</details>

<details><summary><code>10-31-2026-2350-prefill-gemm-v1</code> &mdash; v0.1.1-106-g16fcf7d &mdash; Llama-3.2-1B, smollm2-135m, smollm2-360m-instruct</summary>

config: `prompt_cap=128,gen=128,reps=3,formats=bf16,stages=cross,aggregate,train_steps=20,train_seq=64`

#### Llama-3.2-1B &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 221.5 | 1,407.8 | 1,019.6 | 845.7 |
| decode tok/s | 28.2 | 41.4 | 34.9 | 34.0 |
| TTFT ms | 402 | 63 | 87 | 106 |
| ITL ms | 35.2 | 24.2 | 28.7 | 29.2 |
| peak RSS MB | 4,664 | 2,662 | 2,001 | 595 |
| peak GPU MB | 2,985 | - | 2,588 | 3,283 |
| load ms | 4,045 | - | 1,716 | 2,882 |
| J/token | 0.299 | 0.928 | 0.398 | 0.480 |
| token match % | 100.0 | 100.0 | 1.6 | 100.0 |

#### smollm2-135m &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 972.2 | 8,243.1 | 6,879.9 | 4,089.2 |
| decode tok/s | 43.3 | 160.3 | 231.4 | 102.0 |
| TTFT ms | 91 | 11 | 13 | 22 |
| ITL ms | 23.0 | 6.2 | 4.3 | 9.8 |
| peak RSS MB | 615 | 406 | 705 | 505 |
| peak GPU MB | 562 | - | 340 | 1,154 |
| load ms | 75 | - | 250 | 308 |
| J/token | 0.083 | 0.093 | 0.094 | 0.131 |
| token match % | 100.0 | 100.0 | 28.1 | 30.5 |

#### smollm2-360m-instruct &middot; bf16

| metric | bare.metal | llama.cpp | mlx | torch-mps |
|---|---:|---:|---:|---:|
| prefill tok/s | 510.7 | 3,712.4 | 1,849.5 | 2,031.6 |
| decode tok/s | 34.6 | 113.0 | 82.3 | 61.1 |
| TTFT ms | 172 | 24 | 48 | 44 |
| ITL ms | 28.8 | 8.9 | 12.1 | 16.0 |
| peak RSS MB | 1,563 | 868 | 1,160 | 507 |
| peak GPU MB | 1,243 | - | 835 | 1,160 |
| load ms | 136 | - | 431 | 341 |
| J/token | 0.145 | 0.282 | 0.079 | 0.203 |
| token match % | 100.0 | 100.0 | 19.5 | 19.5 |

</details>

<details><summary><code>11-01-2026-0006-train-grad-accum-v1</code> &mdash; v0.1.1-109-gf20964e &mdash; smollm2-135m</summary>

config: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=train,aggregate,train_steps=20,train_seq=64`

#### smollm2-135m &middot; bare.metal training

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | J/token | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `bf16_b1` | bf16 | 1 | 1 | 64 | 20 | 596.5 | 106.0 | 2.2786 -> 2.6379 | 3105 | 2598 | 0.0726 | PASS (1.1e-06) |
| `bf16_ga4` | bf16 | 1 | 4 | 64 | 20 | 542.6 | 112.3 | 2.2786 -> 2.9371 | 3105 | 2598 | 0.0685 | PASS (0.0e+00) |
| `bf16_b4` | bf16 | 4 | 1 | 64 | 20 | 2266.7 | 112.4 | 2.6485 -> 2.3935 | 3107 | 2598 | 0.0689 | PASS (8.9e-07) |
| `fp32_b1` | fp32 | 1 | 1 | 64 | 20 | 592.5 | 106.8 | 2.2786 -> 2.7159 | 2835 | 2329 | 0.0723 | PASS (7.8e-07) |
| `fp32_ga4` | fp32 | 1 | 4 | 64 | 20 | 551.8 | 113.3 | 2.2786 -> 2.9132 | 2835 | 2329 | 0.0703 | PASS (0.0e+00) |
| `fp32_b4` | fp32 | 4 | 1 | 64 | 20 | 2246.9 | 113.8 | 2.6485 -> 2.4067 | 2836 | 2329 | 0.0719 | PASS (1.8e-07) |

</details>

<details><summary><code>11-01-2026-1255-train-occupancy-v1</code> &mdash; v0.1.1-127-g9569b48 &mdash; smollm2-135m</summary>

config: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=train,aggregate,train_steps=20,train_seq=64`

#### smollm2-135m &middot; bare.metal training

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | J/token | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `bf16_b1` | bf16 | 1 | 1 | 64 | 20 | 384.1 | 163.3 | 2.2786 -> 2.6379 | 3087 | 2598 | - | PASS (9.5e-08) |
| `bf16_ga4` | bf16 | 1 | 4 | 64 | 20 | 330.3 | 184.8 | 2.2786 -> 2.9371 | 3087 | 2598 | - | PASS (0.0e+00) |
| `bf16_b4` | bf16 | 4 | 1 | 64 | 20 | 1407.1 | 181.8 | 2.6485 -> 2.3935 | 3088 | 2598 | - | PASS (1.8e-07) |
| `fp32_b1` | fp32 | 1 | 1 | 64 | 20 | 372.9 | 171.0 | 2.2786 -> 2.7159 | 2817 | 2329 | - | PASS (2.6e-07) |
| `fp32_ga4` | fp32 | 1 | 4 | 64 | 20 | 332.0 | 187.4 | 2.2786 -> 2.9132 | 2817 | 2329 | - | PASS (0.0e+00) |
| `fp32_b4` | fp32 | 4 | 1 | 64 | 20 | 1366.0 | 187.3 | 2.6485 -> 2.4067 | 2818 | 2329 | - | PASS (2.7e-07) |

</details>

<details><summary><code>11-01-2026-1414-train-grad-accum-fix-v1</code> &mdash; v0.1.1-134-g4d0ccef &mdash; smollm2-135m</summary>

config: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=train,aggregate,train_steps=20,train_seq=64`

#### smollm2-135m &middot; bare.metal training

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | J/token | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `bf16_b1` | bf16 | 1 | 1 | 64 | 20 | 381.0 | 166.5 | 2.2786 -> 2.6379 | 3087 | 2598 | - | PASS (2.6e-07) |
| `bf16_ga4` | bf16 | 1 | 4 | 64 | 20 | 328.7 | 184.2 | 2.2786 -> 2.9272 | 3087 | 2598 | - | PASS (0.0e+00) |
| `bf16_b4` | bf16 | 4 | 1 | 64 | 20 | 1408.9 | 182.5 | 2.6485 -> 2.3556 | 3088 | 2598 | - | PASS (5.4e-07) |
| `fp32_b1` | fp32 | 1 | 1 | 64 | 20 | 371.5 | 170.9 | 2.2786 -> 2.7159 | 2817 | 2329 | - | PASS (4.4e-07) |
| `fp32_ga4` | fp32 | 1 | 4 | 64 | 20 | 330.6 | 188.3 | 2.2786 -> 2.9035 | 2817 | 2329 | - | PASS (0.0e+00) |
| `fp32_b4` | fp32 | 4 | 1 | 64 | 20 | 1362.6 | 187.8 | 2.6485 -> 2.3772 | 2818 | 2329 | - | PASS (4.5e-07) |

</details>

_Auto-generated by `tools/index.py` - do not edit by hand._
