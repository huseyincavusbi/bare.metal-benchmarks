# 10-31-2026-2235-mmap-weights-v1

- version: `v0.1.1-101-g2eb12f3`
- settings: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=cross,aggregate,train_steps=20,train_seq=64`

## Llama-3.2-1B

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 70.4 | 27.3 | 1264.52 | 36.43 | 4692 | 8.86 |
| bare.metal | bare.metal__fp16 | fp16 | none | 70.7 | 27.5 | 1259.90 | 36.33 | 5487 | 9.02 |
| bare.metal | bare.metal__q4 | bf16 | q4 | 57.2 | 40.5 | 1557.58 | 25.11 | 4149 | 8.33 |
| bare.metal | bare.metal__q8 | bf16 | q8 | 47.8 | 35.3 | 1861.59 | 28.34 | 4635 | 9.19 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 1390.9 | 39.8 | 63.99 | 25.10 | 2664 | 8.27 |
| llama.cpp | llama.cpp__fp16 | F16 | none | 1425.2 | 39.8 | 62.45 | 25.13 | 2662 | 8.34 |
| llama.cpp | llama.cpp__q4 | Q4_0 | Q4_0 | 1418.8 | 108.7 | 62.73 | 9.20 | 953 | 10.07 |
| llama.cpp | llama.cpp__q8 | Q8_0 | Q8_0 | 1404.1 | 67.6 | 63.38 | 14.80 | 1502 | 9.36 |
| mlx | mlx__bf16 | bf16 | none | 1004.3 | 34.4 | 88.62 | 28.86 | 1504 | 5.83 |
| mlx | mlx__fp16 | fp16 | none | 1033.0 | 36.6 | 86.16 | 27.01 | 2036 | 7.38 |
| mlx | mlx__q4 | int4 | q4 | 1160.6 | 95.3 | 76.68 | 10.29 | 1463 | 5.81 |
| mlx | mlx__q8 | int8 | q8 | 1148.7 | 59.9 | 77.48 | 16.61 | 2081 | 6.14 |
| torch-mps | torch-mps__bf16 | bf16 | none | 840.3 | 32.4 | 106.14 | 30.26 | 595 | 6.08 |
| torch-mps | torch-mps__fp16 | fp16 | none | 802.7 | 31.4 | 111.21 | 31.48 | 5059 | 6.22 |

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

## smollm2-135m

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 355.1 | 42.5 | 247.92 | 23.55 | 615 | 3.88 |
| bare.metal | bare.metal__fp16 | fp16 | none | 349.9 | 42.5 | 251.58 | 23.53 | 615 | 3.85 |
| bare.metal | bare.metal__q4 | bf16 | q4 | 112.6 | 44.8 | 781.62 | 22.26 | 470 | 3.60 |
| bare.metal | bare.metal__q8 | bf16 | q8 | 110.4 | 44.3 | 797.24 | 22.49 | 522 | 5.69 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 6661.2 | 182.8 | 13.21 | 5.47 | 405 | 5.71 |
| llama.cpp | llama.cpp__fp16 | F16 | none | 7846.9 | 176.3 | 11.21 | 5.67 | 403 | 4.77 |
| llama.cpp | llama.cpp__q4 | Q4_0 | Q4_0 | 7954.8 | 227.1 | 11.06 | 4.40 | 226 | 2.92 |
| llama.cpp | llama.cpp__q8 | Q8_0 | Q8_0 | 7861.9 | 219.5 | 11.19 | 4.56 | 276 | 4.20 |
| mlx | mlx__bf16 | bf16 | none | 6812.4 | 202.8 | 12.92 | 4.47 | 705 | 7.94 |
| mlx | mlx__fp16 | fp16 | none | 4045.2 | 133.6 | 21.75 | 7.06 | 705 | 2.76 |
| mlx | mlx__q4 | int4 | q4 | 7068.6 | 358.8 | 12.45 | 2.42 | 515 | 8.30 |
| mlx | mlx__q8 | int8 | q8 | 7082.4 | 281.6 | 12.43 | 3.15 | 582 | 8.78 |
| torch-mps | torch-mps__bf16 | bf16 | none | 4065.8 | 85.9 | 22.21 | 10.70 | 505 | 3.89 |
| torch-mps | torch-mps__fp16 | fp16 | none | 3994.5 | 88.9 | 22.90 | 10.73 | 905 | 4.03 |

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

## smollm2-360m-instruct

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 136.3 | 33.7 | 645.49 | 29.62 | 1563 | 5.99 |
| bare.metal | bare.metal__fp16 | fp16 | none | 136.6 | 33.9 | 644.25 | 29.55 | 1563 | 5.59 |
| bare.metal | bare.metal__q4 | bf16 | q4 | 86.7 | 38.7 | 1015.46 | 25.71 | 1131 | 4.77 |
| bare.metal | bare.metal__q8 | bf16 | q8 | 80.2 | 37.3 | 1097.31 | 26.69 | 1288 | 5.34 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 3656.6 | 108.2 | 24.07 | 9.24 | 866 | 8.91 |
| llama.cpp | llama.cpp__fp16 | F16 | none | 3715.4 | 111.3 | 23.68 | 8.99 | 869 | 8.76 |
| llama.cpp | llama.cpp__q4 | Q4_0 | Q4_0 | 3657.5 | 169.1 | 24.06 | 5.91 | 372 | 4.78 |
| llama.cpp | llama.cpp__q8 | Q8_0 | Q8_0 | 3618.4 | 179.9 | 24.32 | 5.56 | 528 | 9.28 |
| mlx | mlx__bf16 | bf16 | none | 2969.6 | 83.0 | 29.63 | 11.88 | 1159 | 4.63 |
| mlx | mlx__fp16 | fp16 | none | 2931.0 | 84.5 | 30.02 | 11.71 | 1160 | 4.69 |
| mlx | mlx__q4 | int4 | q4 | 3351.0 | 229.9 | 26.26 | 3.96 | 642 | 10.37 |
| mlx | mlx__q8 | int8 | q8 | 3366.2 | 156.3 | 26.14 | 6.05 | 824 | 9.44 |
| torch-mps | torch-mps__bf16 | bf16 | none | 1944.5 | 60.6 | 45.83 | 16.51 | 505 | 6.10 |
| torch-mps | torch-mps__fp16 | fp16 | none | 1945.5 | 59.8 | 45.47 | 16.55 | 1817 | 5.25 |

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

