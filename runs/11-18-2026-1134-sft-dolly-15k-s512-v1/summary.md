# 11-18-2026-1134-sft-dolly-15k-s512-v1

- version: `v0.1.1-233-gaf3f4e0`
- settings: `stages=sft,sft_steps=500,sft_seq=512,dataset=dolly_15000.jsonl,val_split=10,val_limit=200`

## Llama-3.2-1B

### Training

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | W | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | bf16 | 1 | 1 | 512 | 500 | 4117.0 | 119.7 | 2.2124 -> 1.4571 | 7975 | 6159 | - | - |

### SFT

| cfg | template | train | val | val loss | step ms | tok/s | RSS MB | GPU MB | adapter |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | llama3 | 13500 | 200 | 1.9067 | 4117.0 | 119.7 | 7975 | 6159 | Llama-3.2-1B.bin |

## smollm2-135m

### Training

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | W | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | bf16 | 1 | 1 | 512 | 500 | 626.0 | 796.4 | 2.0256 -> 1.6925 | 1181 | 1793 | - | - |

### SFT

| cfg | template | train | val | val loss | step ms | tok/s | RSS MB | GPU MB | adapter |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | chatml | 13500 | 200 | 2.0644 | 626.0 | 796.4 | 1181 | 1793 | smollm2-135m.bin |

