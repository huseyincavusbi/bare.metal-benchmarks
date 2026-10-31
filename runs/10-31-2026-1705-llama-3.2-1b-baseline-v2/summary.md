# 10-31-2026-1705-llama-3.2-1b-baseline-v2

- version: `v0.1.1-63-g566f6dd`
- settings: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=cross,aggregate`

## Llama-3.2-1B

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 18.2 | 15.8 | 4892.65 | 63.27 | 7427 | 6.23 |
| bare.metal | bare.metal__fp16 | fp16 | none | 18.0 | 15.9 | 4957.30 | 63.07 | 7427 | 7.29 |
| bare.metal | bare.metal__q4 | bf16 | q4 | 32.3 | 22.7 | 2756.99 | 40.20 | 5881 | 5.48 |
| bare.metal | bare.metal__q8 | bf16 | q8 | 28.2 | 23.1 | 3153.67 | 43.21 | 7427 | 6.80 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 1415.3 | 39.6 | 62.88 | 25.27 | 2660 | 9.74 |
| llama.cpp | llama.cpp__fp16 | F16 | none | 1425.0 | 39.6 | 62.45 | 25.24 | 2662 | 9.10 |
| llama.cpp | llama.cpp__q4 | Q4_0 | Q4_0 | 1467.8 | 112.6 | 60.64 | 8.88 | 954 | 10.03 |
| llama.cpp | llama.cpp__q8 | Q8_0 | Q8_0 | 1429.5 | 69.2 | 62.26 | 14.46 | 1503 | 10.12 |
| mlx | mlx__bf16 | bf16 | none | 1022.9 | 34.1 | 87.01 | 29.03 | 2898 | 7.30 |
| mlx | mlx__fp16 | fp16 | none | 1037.6 | 36.6 | 85.77 | 27.23 | 2573 | 7.76 |
| mlx | mlx__q4 | int4 | q4 | 1001.5 | 93.6 | 88.87 | 10.64 | 1462 | 4.58 |
| mlx | mlx__q8 | int8 | q8 | 1168.3 | 60.2 | 76.18 | 16.69 | 2079 | 6.96 |
| torch-mps | torch-mps__bf16 | bf16 | none | 848.3 | 33.0 | 105.24 | 30.33 | 595 | 6.27 |
| torch-mps | torch-mps__fp16 | fp16 | none | 849.7 | 33.8 | 105.08 | 29.27 | 5026 | 5.75 |

Output diff vs reference:

- vs `bare.metal__fp16` prompt:identical - token match 100.0% (first-div none)
- vs `bare.metal__q4` prompt:identical - token match 2.3% (first-div 3)
- vs `bare.metal__q8` prompt:identical - token match 100.0% (first-div none)
- vs `llama.cpp__bf16` prompt:identical - token match 100.0% (first-div none)
- vs `llama.cpp__fp16` prompt:identical - token match 100.0% (first-div none)
- vs `llama.cpp__q4` prompt:identical - token match 2.3% (first-div 3)
- vs `llama.cpp__q8` prompt:identical - token match 100.0% (first-div none)
- vs `mlx__bf16` prompt:identical - token match 1.6% (first-div 2)
- vs `mlx__fp16` prompt:identical - token match 1.6% (first-div 2)
- vs `mlx__q4` prompt:identical - token match 2.3% (first-div 3)
- vs `mlx__q8` prompt:identical - token match 100.0% (first-div none)
- vs `torch-mps__bf16` prompt:identical - token match 100.0% (first-div none)
- vs `torch-mps__fp16` prompt:identical - token match 1.6% (first-div 2)

