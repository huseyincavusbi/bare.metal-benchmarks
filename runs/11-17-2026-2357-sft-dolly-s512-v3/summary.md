# 11-17-2026-2357-sft-dolly-s512-v3

- version: `v0.1.1-232-ga57df07`
- settings: `stages=sft,sft_steps=200,sft_seq=512,dataset=dolly_600.jsonl,val_split=10`

## Llama-3.2-1B

### Training

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | W | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | bf16 | 1 | 1 | 512 | 200 | 4081.7 | 124.2 | 2.7480 -> 0.9265 | 1200 | 6159 | - | - |

### SFT

| cfg | template | train | val | val loss | step ms | tok/s | RSS MB | GPU MB | adapter |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | llama3 | 540 | 60 | 2.0351 | 4081.7 | 124.2 | 1200 | 6159 | Llama-3.2-1B.bin |

## smollm2-135m

### Training

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | W | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | bf16 | 1 | 1 | 512 | 200 | 625.6 | 795.9 | 2.7366 -> 0.7994 | 1140 | 1793 | - | - |

### SFT

| cfg | template | train | val | val loss | step ms | tok/s | RSS MB | GPU MB | adapter |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | chatml | 540 | 60 | 2.2762 | 625.6 | 795.9 | 1140 | 1793 | smollm2-135m.bin |

