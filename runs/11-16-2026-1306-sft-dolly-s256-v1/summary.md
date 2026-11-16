# 11-16-2026-1306-sft-dolly-s256-v1

- version: `v0.1.1-225-gd55420a`
- settings: `stages=sft,sft_steps=200,sft_seq=256,dataset=dolly_600.jsonl,val_split=10`

## Llama-3.2-1B

### Training

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | W | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | bf16 | 1 | 1 | 256 | 200 | 2974.4 | 83.7 | 2.9569 -> 0.9211 | 1893 | 5783 | - | - |

### SFT

| cfg | template | train | val | val loss | step ms | tok/s | RSS MB | GPU MB | adapter |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | llama3 | 540 | 60 | 2.0820 | 2974.4 | 83.7 | 1893 | 5783 | Llama-3.2-1B.bin |

## smollm2-135m

### Training

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | W | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | bf16 | 1 | 1 | 256 | 200 | 742.4 | 386.3 | 2.7067 -> 0.7809 | 1238 | 1659 | - | - |

### SFT

| cfg | template | train | val | val loss | step ms | tok/s | RSS MB | GPU MB | adapter |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | chatml | 540 | 60 | 2.3395 | 742.4 | 386.3 | 1238 | 1659 | smollm2-135m.bin |

