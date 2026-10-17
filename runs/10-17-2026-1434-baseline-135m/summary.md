# 10-17-2026-1434-baseline-135m

- version: `v0.1.1`
- settings: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=prep,cross,sweep,aggregate`

## smollm2-135m

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 14.9 | 10.5 | 5915.65 | 94.41 | 1123 | 0.71 |
| bare.metal | bare.metal__fp16 | fp16 | none | 14.6 | 10.5 | 6014.67 | 96.12 | 1119 | 0.68 |
| bare.metal | bare.metal__q4 | bf16 | q4 | 18.7 | 12.1 | 4703.38 | 82.30 | 973 | 0.59 |
| bare.metal | bare.metal__q8 | bf16 | q8 | 19.1 | 12.3 | 4607.07 | 82.02 | 1026 | 0.74 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 8077.7 | 153.5 | 10.89 | 6.51 | 397 | 2.11 |
| llama.cpp | llama.cpp__fp16 | F16 | none | 8199.6 | 198.8 | 10.73 | 5.03 | 397 | 4.30 |
| llama.cpp | llama.cpp__q4 | Q4_0 | Q4_0 | 7842.4 | 255.8 | 11.22 | 3.91 | 217 | 2.92 |
| llama.cpp | llama.cpp__q8 | Q8_0 | Q8_0 | 7901.3 | 206.1 | 11.14 | 4.85 | 271 | 3.28 |
| mlx | mlx__bf16 | bf16 | none | 4047.7 | 155.2 | 21.74 | 6.10 | 705 | 2.55 |
| mlx | mlx__fp16 | fp16 | none | 3620.0 | 168.8 | 24.31 | 5.68 | 705 | 4.58 |
| mlx | mlx__q4 | int4 | q4 | 7016.2 | 408.2 | 12.54 | 2.43 | 514 | 9.15 |
| mlx | mlx__q8 | int8 | q8 | 7048.3 | 319.1 | 12.49 | 3.12 | 581 | 8.98 |
| torch-mps | torch-mps__bf16 | bf16 | none | 3350.7 | 84.0 | 26.93 | 10.61 | 504 | 2.84 |
| torch-mps | torch-mps__fp16 | fp16 | none | 4005.7 | 82.4 | 22.22 | 12.17 | 906 | 2.69 |

Output diff vs reference:

- vs `bare.metal__fp16` prompt:identical - token match 100.0% (first-div none)
- vs `bare.metal__q4` prompt:identical - token match 6.2% (first-div 8)
- vs `bare.metal__q8` prompt:identical - token match 11.7% (first-div 15)
- vs `llama.cpp__bf16` prompt:identical - token match 100.0% (first-div none)
- vs `llama.cpp__fp16` prompt:identical - token match 100.0% (first-div none)
- vs `llama.cpp__q4` prompt:identical - token match 6.2% (first-div 8)
- vs `llama.cpp__q8` prompt:identical - token match 11.7% (first-div 15)
- vs `mlx__bf16` prompt:identical - token match 28.1% (first-div 36)
- vs `mlx__fp16` prompt:identical - token match 100.0% (first-div none)
- vs `mlx__q4` prompt:identical - token match 6.2% (first-div 8)
- vs `mlx__q8` prompt:identical - token match 12.5% (first-div 16)
- vs `torch-mps__bf16` prompt:identical - token match 30.5% (first-div 39)
- vs `torch-mps__fp16` prompt:identical - token match 100.0% (first-div none)

Sweep configs: `p1024_bf16, p128_bf16, p128_fp16, p128_q4, p128_q8, p512_bf16`

