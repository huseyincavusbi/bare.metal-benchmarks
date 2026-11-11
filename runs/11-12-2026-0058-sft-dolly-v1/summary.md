# 11-12-2026-0058-sft-dolly-v1

- version: `v0.1.1-203-g5dc0c76`
- settings: `stages=sft,sft_steps=200,sft_seq=128,dataset=dolly_600.jsonl,val_split=10`

## Llama-3.2-1B

### Training

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | W | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | bf16 | 1 | 1 | 128 | 200 | 1570.4 | 81.8 | 3.1117 -> 1.0651 | 8062 | 4178 | - | - |

### SFT

| cfg | template | train | val | val loss | step ms | tok/s | RSS MB | GPU MB | adapter |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | llama3 | 540 | 60 | 2.1786 | 1570.4 | 81.8 | 8062 | 4178 | Llama-3.2-1B.bin |

## smollm2-135m

### Training

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | W | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | bf16 | 1 | 1 | 128 | 200 | 352.0 | 375.8 | 2.7897 -> 0.8955 | 1283 | 986 | - | - |

### SFT

| cfg | template | train | val | val loss | step ms | tok/s | RSS MB | GPU MB | adapter |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | chatml | 540 | 60 | 2.5007 | 352.0 | 375.8 | 1283 | 986 | smollm2-135m.bin |

