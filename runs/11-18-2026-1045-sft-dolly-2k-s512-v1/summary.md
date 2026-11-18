# 11-18-2026-1045-sft-dolly-2k-s512-v1

- version: `v0.1.1-233-gaf3f4e0`
- settings: `stages=sft,sft_steps=500,sft_seq=512,dataset=dolly_2000.jsonl,val_split=10`

## Llama-3.2-1B

### Training

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | W | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | bf16 | 1 | 1 | 512 | 500 | 4088.2 | 124.0 | 2.5426 -> 1.2813 | 7956 | 6159 | - | - |

### SFT

| cfg | template | train | val | val loss | step ms | tok/s | RSS MB | GPU MB | adapter |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | llama3 | 1800 | 200 | 1.9102 | 4088.2 | 124.0 | 7956 | 6159 | Llama-3.2-1B.bin |

## smollm2-135m

### Training

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | W | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | bf16 | 1 | 1 | 512 | 500 | 645.2 | 774.2 | 4.1091 -> 1.5315 | 1164 | 1793 | - | - |

### SFT

| cfg | template | train | val | val loss | step ms | tok/s | RSS MB | GPU MB | adapter |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | chatml | 1800 | 200 | 2.0855 | 645.2 | 774.2 | 1164 | 1793 | smollm2-135m.bin |

