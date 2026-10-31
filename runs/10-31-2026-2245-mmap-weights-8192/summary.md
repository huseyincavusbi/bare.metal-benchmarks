# 10-31-2026-2245-mmap-weights-8192

- version: `v0.1.1-101-g2eb12f3`
- settings: `prompt_cap=128,gen=128,reps=3,formats=bf16,stages=cross,aggregate,train_steps=20,train_seq=64`

## smollm2-135m

| engine | file | prec | q | pre t/s | dec t/s | ttft ms | itl ms | rss MB | W |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| bare.metal | bare.metal__bf16 | bf16 | none | 346.9 | 42.5 | 253.74 | 23.50 | 615 | 3.87 |
| llama.cpp | llama.cpp__bf16 | BF16 | none | 7834.3 | 178.2 | 11.23 | 5.61 | 403 | 5.32 |
| mlx | mlx__bf16 | bf16 | none | 4874.0 | 117.2 | 18.05 | 8.12 | 705 | 2.20 |
| torch-mps | torch-mps__bf16 | bf16 | none | 3948.8 | 92.9 | 22.51 | 10.45 | 504 | 3.89 |

Output diff vs reference:

- vs `llama.cpp__bf16` prompt:identical - token match 100.0% (first-div none)
- vs `mlx__bf16` prompt:identical - token match 28.1% (first-div 36)
- vs `torch-mps__bf16` prompt:identical - token match 30.5% (first-div 39)

