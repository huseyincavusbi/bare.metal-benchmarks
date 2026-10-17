# 10-17-2026-1511-baseline-360m

- version: `v0.1.1`
- settings: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=prep,cross,sweep,aggregate`

## smollm2-360m-instruct

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 11.2 | 8.4 | 7886.40 | 118.65 | 2924 | 0.81 |
| bare.metal | bare.metal__fp16 | fp16 | none | 11.1 | 8.3 | 7911.47 | 119.60 | 2940 | 0.76 |
| bare.metal | bare.metal__q4 | bf16 | q4 | 15.7 | 10.6 | 5616.89 | 94.88 | 2508 | 0.69 |
| bare.metal | bare.metal__q8 | bf16 | q8 | 15.1 | 10.4 | 5820.08 | 96.56 | 2666 | 0.74 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 3674.9 | 100.7 | 23.95 | 9.93 | 862 | 4.12 |
| llama.cpp | llama.cpp__fp16 | F16 | none | 3751.7 | 100.7 | 23.46 | 9.93 | 861 | 3.69 |
| llama.cpp | llama.cpp__q4 | Q4_0 | Q4_0 | 3737.9 | 150.4 | 23.54 | 6.65 | 366 | 3.18 |
| llama.cpp | llama.cpp__q8 | Q8_0 | Q8_0 | 3664.7 | 131.3 | 24.01 | 7.61 | 523 | 3.34 |
| mlx | mlx__bf16 | bf16 | none | 2690.9 | 97.2 | 32.70 | 10.72 | 1160 | 3.20 |
| mlx | mlx__fp16 | fp16 | none | 1864.5 | 77.8 | 47.20 | 12.74 | 1160 | 1.94 |
| mlx | mlx__q4 | int4 | q4 | 3355.2 | 256.4 | 26.23 | 3.90 | 644 | 10.07 |
| mlx | mlx__q8 | int8 | q8 | 1968.6 | 105.3 | 44.70 | 9.10 | 824 | 2.18 |
| torch-mps | torch-mps__bf16 | bf16 | none | 1341.4 | 46.8 | 65.98 | 21.16 | 511 | 2.18 |
| torch-mps | torch-mps__fp16 | fp16 | none | 1539.0 | 49.7 | 57.50 | 20.15 | 1817 | 2.34 |

Output diff vs reference:

- vs `bare.metal__fp16` prompt:identical - token match 100.0% (first-div none)
- vs `bare.metal__q4` prompt:identical - token match 1.6% (first-div 2)
- vs `bare.metal__q8` prompt:identical - token match 38.3% (first-div 49)
- vs `llama.cpp__bf16` prompt:identical - token match 100.0% (first-div none)
- vs `llama.cpp__fp16` prompt:identical - token match 100.0% (first-div none)
- vs `llama.cpp__q4` prompt:identical - token match 1.6% (first-div 2)
- vs `llama.cpp__q8` prompt:identical - token match 35.2% (first-div 45)
- vs `mlx__bf16` prompt:identical - token match 19.5% (first-div 25)
- vs `mlx__fp16` prompt:identical - token match 100.0% (first-div none)
- vs `mlx__q4` prompt:identical - token match 1.6% (first-div 2)
- vs `mlx__q8` prompt:identical - token match 5.5% (first-div 7)
- vs `torch-mps__bf16` prompt:identical - token match 19.5% (first-div 25)
- vs `torch-mps__fp16` prompt:identical - token match 100.0% (first-div none)

Sweep configs: `p1024_bf16, p128_bf16, p128_fp16, p128_q4, p128_q8, p512_bf16`

