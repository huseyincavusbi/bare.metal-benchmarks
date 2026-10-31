# 10-31-2026-2350-prefill-gemm-v1

- version: `v0.1.1-106-g16fcf7d`
- settings: `prompt_cap=128,gen=128,reps=3,formats=bf16,stages=cross,aggregate,train_steps=20,train_seq=64`

## Llama-3.2-1B

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 221.5 | 28.2 | 402.08 | 35.22 | 4664 | 7.83 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 1407.8 | 41.4 | 63.22 | 24.17 | 2662 | 7.83 |
| mlx | mlx__bf16 | bf16 | none | 1019.6 | 34.9 | 87.29 | 28.65 | 2001 | 4.55 |
| torch-mps | torch-mps__bf16 | bf16 | none | 845.7 | 34.0 | 105.50 | 29.22 | 595 | 5.29 |

Output diff vs reference:

- vs `llama.cpp__bf16` prompt:identical - token match 100.0% (first-div none)
- vs `mlx__bf16` prompt:identical - token match 1.6% (first-div 2)
- vs `torch-mps__bf16` prompt:identical - token match 100.0% (first-div none)

## smollm2-135m

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 972.2 | 43.3 | 90.60 | 23.00 | 615 | 3.52 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 8243.1 | 160.3 | 10.68 | 6.24 | 406 | 3.18 |
| mlx | mlx__bf16 | bf16 | none | 6879.9 | 231.4 | 12.79 | 4.32 | 705 | 7.15 |
| torch-mps | torch-mps__bf16 | bf16 | none | 4089.2 | 102.0 | 21.75 | 9.81 | 505 | 4.30 |

Output diff vs reference:

- vs `llama.cpp__bf16` prompt:identical - token match 100.0% (first-div none)
- vs `mlx__bf16` prompt:identical - token match 28.1% (first-div 36)
- vs `torch-mps__bf16` prompt:identical - token match 30.5% (first-div 39)

## smollm2-360m-instruct

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 510.7 | 34.6 | 172.42 | 28.84 | 1563 | 4.83 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 3712.4 | 113.0 | 23.70 | 8.85 | 868 | 6.59 |
| mlx | mlx__bf16 | bf16 | none | 1849.5 | 82.3 | 47.58 | 12.11 | 1160 | 2.12 |
| torch-mps | torch-mps__bf16 | bf16 | none | 2031.6 | 61.1 | 43.54 | 16.03 | 507 | 4.04 |

Output diff vs reference:

- vs `llama.cpp__bf16` prompt:identical - token match 100.0% (first-div none)
- vs `mlx__bf16` prompt:identical - token match 19.5% (first-div 25)
- vs `torch-mps__bf16` prompt:identical - token match 19.5% (first-div 25)

