# 10-31-2026-2313-quant-prefill-v1

- version: `v0.1.1-106-g23dc1ba`
- settings: `prompt_cap=128,gen=128,reps=3,formats=bf16,q4,q8,stages=cross,sweep,aggregate,train_steps=20,train_seq=64`

## Llama-3.2-1B

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 72.8 | 27.8 | 1223.23 | 36.08 | 3460 | 8.96 |
| bare.metal | bare.metal__q4 | bf16 | q4 | 148.5 | 41.5 | 599.73 | 24.12 | 4149 | 8.16 |
| bare.metal | bare.metal__q8 | bf16 | q8 | 176.6 | 36.1 | 504.05 | 27.80 | 4635 | 9.41 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 1417.6 | 41.2 | 62.78 | 24.27 | 2662 | 7.74 |
| llama.cpp | llama.cpp__q4 | Q4_0 | Q4_0 | 1463.4 | 110.9 | 60.82 | 9.02 | 953 | 9.16 |
| llama.cpp | llama.cpp__q8 | Q8_0 | Q8_0 | 1425.7 | 70.7 | 62.43 | 14.14 | 1502 | 8.88 |
| mlx | mlx__bf16 | bf16 | none | 1032.2 | 34.8 | 86.22 | 28.60 | 1157 | 5.20 |
| mlx | mlx__q4 | int4 | q4 | 1157.1 | 100.1 | 76.92 | 9.91 | 1464 | 5.39 |
| mlx | mlx__q8 | int8 | q8 | 1097.9 | 59.0 | 81.06 | 16.68 | 2081 | 4.79 |
| torch-mps | torch-mps__bf16 | bf16 | none | 849.9 | 33.9 | 104.97 | 29.22 | 595 | 5.94 |

Output diff vs reference:

- vs `bare.metal__q4` prompt:identical - token match 2.3% (first-div 3)
- vs `bare.metal__q8` prompt:identical - token match 100.0% (first-div none)
- vs `llama.cpp__bf16` prompt:identical - token match 100.0% (first-div none)
- vs `llama.cpp__q4` prompt:identical - token match 2.3% (first-div 3)
- vs `llama.cpp__q8` prompt:identical - token match 100.0% (first-div none)
- vs `mlx__bf16` prompt:identical - token match 1.6% (first-div 2)
- vs `mlx__q4` prompt:identical - token match 2.3% (first-div 3)
- vs `mlx__q8` prompt:identical - token match 100.0% (first-div none)
- vs `torch-mps__bf16` prompt:identical - token match 100.0% (first-div none)

Sweep configs: `p1024_bf16, p1024_q4, p1024_q8, p128_bf16, p128_fp16, p128_q4, p128_q8, p512_bf16, p512_q4, p512_q8`

## smollm2-135m

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 383.1 | 43.2 | 229.75 | 23.10 | 615 | 4.15 |
| bare.metal | bare.metal__q4 | bf16 | q4 | 824.3 | 45.2 | 106.83 | 22.04 | 470 | 3.67 |
| bare.metal | bare.metal__q8 | bf16 | q8 | 932.0 | 44.9 | 94.50 | 22.22 | 522 | 3.40 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 7433.5 | 171.0 | 11.84 | 5.85 | 402 | 4.18 |
| llama.cpp | llama.cpp__q4 | Q4_0 | Q4_0 | 7865.9 | 245.8 | 11.19 | 4.07 | 223 | 4.04 |
| llama.cpp | llama.cpp__q8 | Q8_0 | Q8_0 | 6001.0 | 216.9 | 14.66 | 4.61 | 276 | 3.12 |
| mlx | mlx__bf16 | bf16 | none | 6649.9 | 196.8 | 13.23 | 4.96 | 705 | 3.27 |
| mlx | mlx__q4 | int4 | q4 | 6983.3 | 408.6 | 12.60 | 2.43 | 515 | 9.60 |
| mlx | mlx__q8 | int8 | q8 | 7170.8 | 316.0 | 12.27 | 3.12 | 581 | 9.23 |
| torch-mps | torch-mps__bf16 | bf16 | none | 4113.5 | 99.5 | 21.62 | 9.89 | 505 | 4.12 |

Output diff vs reference:

- vs `bare.metal__q4` prompt:identical - token match 6.2% (first-div 8)
- vs `bare.metal__q8` prompt:identical - token match 11.7% (first-div 15)
- vs `llama.cpp__bf16` prompt:identical - token match 100.0% (first-div none)
- vs `llama.cpp__q4` prompt:identical - token match 6.2% (first-div 8)
- vs `llama.cpp__q8` prompt:identical - token match 11.7% (first-div 15)
- vs `mlx__bf16` prompt:identical - token match 28.1% (first-div 36)
- vs `mlx__q4` prompt:identical - token match 6.2% (first-div 8)
- vs `mlx__q8` prompt:identical - token match 12.5% (first-div 16)
- vs `torch-mps__bf16` prompt:identical - token match 30.5% (first-div 39)

Sweep configs: `p1024_bf16, p1024_q4, p1024_q8, p128_bf16, p128_fp16, p128_q4, p128_q8, p512_bf16, p512_q4, p512_q8`

## smollm2-360m-instruct

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 142.9 | 34.4 | 615.81 | 29.32 | 1563 | 7.02 |
| bare.metal | bare.metal__q4 | bf16 | q4 | 379.1 | 39.1 | 232.19 | 25.59 | 1131 | 4.43 |
| bare.metal | bare.metal__q8 | bf16 | q8 | 418.5 | 37.7 | 210.35 | 26.80 | 1289 | 5.43 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 3717.1 | 100.3 | 23.67 | 9.97 | 867 | 5.27 |
| llama.cpp | llama.cpp__q4 | Q4_0 | Q4_0 | 3680.0 | 144.4 | 23.91 | 6.93 | 370 | 3.21 |
| llama.cpp | llama.cpp__q8 | Q8_0 | Q8_0 | 3521.0 | 135.1 | 24.99 | 7.41 | 530 | 6.01 |
| mlx | mlx__bf16 | bf16 | none | 1846.9 | 83.7 | 47.65 | 11.85 | 1160 | 2.18 |
| mlx | mlx__q4 | int4 | q4 | 3392.7 | 247.0 | 25.94 | 3.96 | 644 | 12.07 |
| mlx | mlx__q8 | int8 | q8 | 2140.5 | 114.2 | 41.11 | 8.17 | 822 | 3.64 |
| torch-mps | torch-mps__bf16 | bf16 | none | 2062.0 | 62.3 | 42.92 | 16.01 | 506 | 4.18 |

Output diff vs reference:

- vs `bare.metal__q4` prompt:identical - token match 1.6% (first-div 2)
- vs `bare.metal__q8` prompt:identical - token match 38.3% (first-div 49)
- vs `llama.cpp__bf16` prompt:identical - token match 100.0% (first-div none)
- vs `llama.cpp__q4` prompt:identical - token match 1.6% (first-div 2)
- vs `llama.cpp__q8` prompt:identical - token match 35.2% (first-div 45)
- vs `mlx__bf16` prompt:identical - token match 19.5% (first-div 25)
- vs `mlx__q4` prompt:identical - token match 1.6% (first-div 2)
- vs `mlx__q8` prompt:identical - token match 5.5% (first-div 7)
- vs `torch-mps__bf16` prompt:identical - token match 19.5% (first-div 25)

Sweep configs: `p1024_bf16, p1024_q4, p1024_q8, p128_bf16, p128_fp16, p128_q4, p128_q8, p512_bf16, p512_q4, p512_q8`

