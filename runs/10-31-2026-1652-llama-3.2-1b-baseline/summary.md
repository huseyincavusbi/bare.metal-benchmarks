# 10-31-2026-1652-llama-3.2-1b-baseline

- version: `v0.1.1-58-gcb405d5`
- settings: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=prep,cross,aggregate`

## Llama-3.2-1B

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 18.3 | 16.0 | 4814.40 | 62.79 | 6014 | 7.28 |
| bare.metal | bare.metal__fp16 | fp16 | none | 18.0 | 15.9 | 4888.90 | 63.21 | 7427 | 7.45 |
| bare.metal | bare.metal__q4 | bf16 | q4 | 32.4 | 25.7 | 2719.81 | 38.88 | 5851 | 6.68 |
| bare.metal | bare.metal__q8 | bf16 | q8 | 28.0 | 22.6 | 3138.57 | 43.95 | 7427 | 6.45 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 1414.5 | 40.4 | 62.92 | 24.78 | 2662 | 7.94 |
| llama.cpp | llama.cpp__fp16 | F16 | none | 1432.6 | 40.7 | 62.13 | 24.60 | 2661 | 8.71 |
| llama.cpp | llama.cpp__q4 | Q4_0 | Q4_0 | 1455.8 | 114.6 | 61.14 | 8.73 | 954 | 9.19 |
| llama.cpp | llama.cpp__q8 | Q8_0 | Q8_0 | 1432.5 | 70.0 | 62.13 | 14.29 | 1501 | 10.14 |
| mlx | mlx__bf16 | bf16 | none | 1039.5 | 37.2 | 85.61 | 26.73 | 3063 | 7.40 |
| mlx | mlx__fp16 | fp16 | none | 1040.2 | 36.9 | 85.56 | 27.11 | 2474 | 7.71 |
| mlx | mlx__q4 | int4 | q4 | 1017.3 | 93.3 | 87.49 | 10.66 | 1462 | 3.87 |
| mlx | mlx__q8 | int8 | q8 | 1102.2 | 58.6 | 80.75 | 17.00 | 2080 | 4.68 |
| torch-mps | torch-mps__bf16 | bf16 | none | 852.9 | 33.6 | 104.68 | 29.75 | 594 | 5.97 |
| torch-mps | torch-mps__fp16 | fp16 | none | 847.7 | 32.4 | 105.32 | 30.54 | 5415 | 6.34 |

Output diff vs reference:

- vs `bare.metal__fp16` prompt:identical - token match 100.0% (first-div none)
- vs `bare.metal__q4` prompt:identical - token match 2.3% (first-div 3)
- vs `bare.metal__q8` prompt:identical - token match 100.0% (first-div none)
- vs `llama.cpp__bf16` prompt:first-div@0 - token match 0.0% (first-div 0)
- vs `llama.cpp__fp16` prompt:first-div@0 - token match 0.0% (first-div 0)
- vs `llama.cpp__q4` prompt:first-div@0 - token match 0.0% (first-div 0)
- vs `llama.cpp__q8` prompt:first-div@0 - token match 0.0% (first-div 0)
- vs `mlx__bf16` prompt:first-div@0 - token match 1.6% (first-div 2)
- vs `mlx__fp16` prompt:first-div@0 - token match 1.6% (first-div 2)
- vs `mlx__q4` prompt:first-div@0 - token match 2.3% (first-div 3)
- vs `mlx__q8` prompt:first-div@0 - token match 3.9% (first-div 5)
- vs `torch-mps__bf16` prompt:first-div@0 - token match 3.9% (first-div 5)
- vs `torch-mps__fp16` prompt:first-div@0 - token match 1.6% (first-div 2)

