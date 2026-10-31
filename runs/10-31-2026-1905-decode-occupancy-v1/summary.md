# 10-31-2026-1905-decode-occupancy-v1

- version: `v0.1.1-78-gfc9d700`
- settings: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=prep,cross,sweep,aggregate`

## Llama-3.2-1B

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 73.6 | 28.3 | 1210.08 | 35.33 | 6056 | 8.71 |
| bare.metal | bare.metal__fp16 | fp16 | none | 73.0 | 28.4 | 1219.11 | 35.33 | 7427 | 8.62 |
| bare.metal | bare.metal__q4 | bf16 | q4 | 59.7 | 41.6 | 1490.18 | 24.03 | 7427 | 7.97 |
| bare.metal | bare.metal__q8 | bf16 | q8 | 49.4 | 36.4 | 1802.31 | 27.50 | 7427 | 8.67 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 1420.0 | 41.5 | 62.68 | 24.09 | 2661 | 7.91 |
| llama.cpp | llama.cpp__fp16 | F16 | none | 1420.0 | 41.6 | 62.68 | 24.01 | 2660 | 7.96 |
| llama.cpp | llama.cpp__q4 | Q4_0 | Q4_0 | 1462.6 | 115.2 | 60.85 | 8.68 | 953 | 9.36 |
| llama.cpp | llama.cpp__q8 | Q8_0 | Q8_0 | 1423.0 | 71.8 | 62.54 | 13.92 | 1501 | 9.04 |
| mlx | mlx__bf16 | bf16 | none | 1010.4 | 35.0 | 88.08 | 28.46 | 3239 | 4.53 |
| mlx | mlx__fp16 | fp16 | none | 1012.9 | 35.2 | 87.87 | 28.39 | 3237 | 4.55 |
| mlx | mlx__q4 | int4 | q4 | 1124.6 | 94.9 | 79.14 | 10.33 | 1463 | 3.88 |
| mlx | mlx__q8 | int8 | q8 | 1087.1 | 60.0 | 81.87 | 16.65 | 2082 | 4.43 |
| torch-mps | torch-mps__bf16 | bf16 | none | 853.8 | 34.6 | 104.49 | 28.72 | 595 | 5.34 |
| torch-mps | torch-mps__fp16 | fp16 | none | 850.7 | 34.2 | 104.86 | 29.07 | 5488 | 5.69 |

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

Sweep configs: `p1024_bf16, p128_bf16, p128_fp16, p128_q4, p128_q8, p512_bf16`

## smollm2-135m

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 380.0 | 43.0 | 231.64 | 23.09 | 873 | 3.62 |
| bare.metal | bare.metal__fp16 | fp16 | none | 382.6 | 43.0 | 230.07 | 23.03 | 872 | 3.92 |
| bare.metal | bare.metal__q4 | bf16 | q4 | 116.5 | 45.4 | 755.72 | 22.03 | 820 | 3.24 |
| bare.metal | bare.metal__q8 | bf16 | q8 | 114.7 | 45.1 | 767.34 | 22.17 | 820 | 3.59 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 7874.2 | 153.1 | 11.18 | 6.53 | 402 | 3.35 |
| llama.cpp | llama.cpp__fp16 | F16 | none | 7896.8 | 157.1 | 11.14 | 6.37 | 402 | 3.36 |
| llama.cpp | llama.cpp__q4 | Q4_0 | Q4_0 | 8381.7 | 222.2 | 10.50 | 4.50 | 224 | 2.45 |
| llama.cpp | llama.cpp__q8 | Q8_0 | Q8_0 | 7293.1 | 172.4 | 12.07 | 5.80 | 277 | 2.85 |
| mlx | mlx__bf16 | bf16 | none | 6656.0 | 225.8 | 13.22 | 4.44 | 705 | 5.21 |
| mlx | mlx__fp16 | fp16 | none | 6866.3 | 231.9 | 12.82 | 4.31 | 705 | 7.02 |
| mlx | mlx__q4 | int4 | q4 | 7070.2 | 417.0 | 12.45 | 2.40 | 515 | 9.69 |
| mlx | mlx__q8 | int8 | q8 | 7110.9 | 320.7 | 12.38 | 3.09 | 581 | 9.59 |
| torch-mps | torch-mps__bf16 | bf16 | none | 4088.5 | 101.1 | 21.76 | 9.85 | 505 | 3.91 |
| torch-mps | torch-mps__fp16 | fp16 | none | 4083.7 | 101.7 | 21.84 | 9.86 | 905 | 4.00 |

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

## smollm2-360m-instruct

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 143.0 | 34.5 | 615.33 | 28.90 | 2260 | 5.16 |
| bare.metal | bare.metal__fp16 | fp16 | none | 143.6 | 34.6 | 613.10 | 28.75 | 2260 | 5.18 |
| bare.metal | bare.metal__q4 | bf16 | q4 | 90.3 | 39.4 | 974.82 | 25.39 | 2183 | 4.44 |
| bare.metal | bare.metal__q8 | bf16 | q8 | 84.1 | 38.3 | 1046.96 | 26.09 | 2183 | 5.13 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 3662.3 | 116.9 | 24.03 | 8.55 | 867 | 7.85 |
| llama.cpp | llama.cpp__fp16 | F16 | none | 3663.5 | 116.9 | 24.02 | 8.55 | 867 | 7.63 |
| llama.cpp | llama.cpp__q4 | Q4_0 | Q4_0 | 3711.0 | 147.6 | 23.71 | 6.77 | 371 | 3.36 |
| llama.cpp | llama.cpp__q8 | Q8_0 | Q8_0 | 3633.3 | 185.5 | 24.22 | 5.39 | 529 | 10.12 |
| mlx | mlx__bf16 | bf16 | none | 1934.8 | 83.5 | 45.48 | 12.26 | 1160 | 2.17 |
| mlx | mlx__fp16 | fp16 | none | 1911.8 | 82.5 | 46.03 | 12.21 | 1160 | 1.97 |
| mlx | mlx__q4 | int4 | q4 | 3383.9 | 255.2 | 26.01 | 3.90 | 644 | 10.82 |
| mlx | mlx__q8 | int8 | q8 | 3396.6 | 169.2 | 25.91 | 5.86 | 824 | 9.36 |
| torch-mps | torch-mps__bf16 | bf16 | none | 2084.4 | 62.6 | 42.45 | 15.95 | 506 | 4.15 |
| torch-mps | torch-mps__fp16 | fp16 | none | 2085.0 | 61.9 | 42.76 | 16.04 | 1817 | 4.37 |

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

