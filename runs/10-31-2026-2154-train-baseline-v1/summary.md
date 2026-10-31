# 10-31-2026-2154-train-baseline-v1

- version: `v0.1.1-84-g2aba0ca`
- settings: `prompt_cap=128,gen=128,reps=3,formats=bf16,fp16,q8,q4,stages=train,aggregate,train_steps=20,train_seq=64`

## smollm2-135m

### Training

| cfg | prec | B | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | W | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_b1 | bf16 | 1 | 64 | 20 | 598.9 | 105.6 | 2.2786 -> 2.6379 | 3105 | 2598 | 7.31 | PASS (5.7e-07) |
| bf16_b4 | bf16 | 4 | 64 | 20 | 2276.0 | 112.1 | 2.6485 -> 2.3935 | 3105 | 2598 | 8.46 | PASS (3.6e-07) |
| fp32_b1 | fp32 | 1 | 64 | 20 | 591.4 | 107.1 | 2.2786 -> 2.7159 | 2835 | 2329 | 10.12 | PASS (1.0e-07) |
| fp32_b4 | fp32 | 4 | 64 | 20 | 2247.6 | 113.3 | 2.6485 -> 2.4067 | 2836 | 2329 | 8.99 | PASS (9.0e-08) |

