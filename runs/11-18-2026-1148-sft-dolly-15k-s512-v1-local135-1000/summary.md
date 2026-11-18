# 11-18-2026-1148-sft-dolly-15k-s512-v1-local135-1000

- version: `v0.1.1-239-g350746e`
- settings: `stages=sft,sft_steps=1000,sft_seq=512,dataset=dolly_15000.jsonl,val_split=10,val_limit=200`

## smollm2-135m

### Training

| cfg | prec | B | G | S | steps | step ms | tok/s | loss | RSS MB | GPU MB | W | parity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | bf16 | 1 | 1 | 512 | 1000 | 649.8 | 768.6 | 2.0256 -> 2.2112 | 1135 | 1793 | - | - |

### SFT

| cfg | template | train | val | val loss | step ms | tok/s | RSS MB | GPU MB | adapter |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| bf16_sft | chatml | 13500 | 200 | 2.0333 | 649.8 | 768.6 | 1135 | 1793 | smollm2-135m.bin |

