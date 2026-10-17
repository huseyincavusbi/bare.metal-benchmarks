#!/usr/bin/env python3
"""Regenerate index.json and README.md from runs/* in this results repo.

Each run directory must contain run.json and grand.json (as published by
bench/run_benchmark.sh from the main bare.metal repository).

Usage:
  tools/index.py            # rewrite index.json + README.md
  tools/index.py --check    # exit 1 if they are stale (for CI)
"""
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS_DIR = os.path.join(ROOT, "runs")
SCHEMA = "baremetal.results-index/v1"
REF_ENGINE = "bare.metal"
MAIN_FMTS = ("bf16", "q4")


def num(d, *keys):
    for k in keys:
        if not isinstance(d, dict):
            return None
        d = d.get(k)
    return d


def match_pct(ref_ids, ids):
    if not ref_ids or not ids:
        return None
    n = min(len(ref_ids), len(ids))
    first = next((i for i in range(n) if ref_ids[i] != ids[i]), None)
    return round(100.0 * (first if first is not None else n) / max(n, 1), 1)


def variant_stats(res, match):
    rss = num(res, "memory", "rss_peak_bytes")
    gpu = num(res, "memory", "gpu_peak_bytes")
    return {
        "prefill_tok_s": num(res, "prefill", "tok_s", "p50"),
        "decode_tok_s": num(res, "decode", "tok_s", "p50"),
        "ttft_ms": num(res, "ttft_ms", "p50"),
        "itl_ms": num(res, "itl_ms", "p50"),
        "rss_mb": round(rss / 1e6, 0) if rss else None,
        "gpu_mb": round(gpu / 1e6, 0) if gpu else None,
        "j_per_token": num(res, "energy", "j_per_token"),
        "match_pct": match,
    }


def model_headline(body):
    engines = (body.get("engines") or {})
    ref_ids = num(engines, REF_ENGINE, "variants", "bf16", "results", "generated_token_ids")
    out = {}
    for fmt in sorted({f for e in engines.values() for f in (e.get("variants") or {})}):
        per_engine = {}
        for eng, ebody in sorted(engines.items()):
            v = (ebody.get("variants") or {}).get(fmt)
            if not v:
                continue
            res = v.get("results") or {}
            if eng == REF_ENGINE and fmt == "bf16":
                m = 100.0
            else:
                m = match_pct(ref_ids, res.get("generated_token_ids"))
            per_engine[eng] = variant_stats(res, m)
        if per_engine:
            out[fmt] = per_engine
    return out


def sweep_rows(body):
    rows = []
    for cfg, v in sorted((body.get("sweep") or {}).items()):
        res = v.get("results") or {}
        conf = v.get("config") or {}
        rows.append({
            "cfg": cfg,
            "prompt_tokens": conf.get("prompt_tokens"),
            "prefill_tok_s": num(res, "prefill", "tok_s", "p50"),
            "decode_tok_s": num(res, "decode", "tok_s", "p50"),
            "ttft_ms": num(res, "ttft_ms", "p50"),
            "itl_ms": num(res, "itl_ms", "p50"),
        })
    return rows


def load_runs():
    runs = []
    for d in sorted(glob.glob(os.path.join(RUNS_DIR, "*"))):
        rj, gj = os.path.join(d, "run.json"), os.path.join(d, "grand.json")
        if not (os.path.isfile(rj) and os.path.isfile(gj)):
            continue
        try:
            run = json.load(open(rj))
            grand = json.load(open(gj))
        except Exception:
            continue
        name = run.get("name") or os.path.basename(d)
        models = (grand.get("models") or {})
        kind = ("baseline" if "baseline" in name
                else "smoke" if "smoke" in name else "run")
        runs.append({
            "folder": os.path.basename(d),
            "name": name,
            "date": name[:10],
            "kind": kind,
            "version": (run.get("version") or {}).get("describe"),
            "commit": (run.get("version") or {}).get("commit"),
            "settings": run.get("settings"),
            "models": sorted(models.keys()),
            "engines": sorted({e for m in models.values() for e in (m.get("engines") or {})}),
            "headline": {stem: model_headline(b) for stem, b in models.items()},
            "sweep": {stem: sweep_rows(b) for stem, b in models.items()},
        })
    return runs


def f(x, nd=1, dash="-"):
    return dash if x is None else f"{x:.{nd}f}"


def ratio(best, ours):
    if not best or not ours:
        return None
    return best / ours


def best_engine(per_engine, key, mode="max"):
    cand = {e: v for e, v in per_engine.items() if e != REF_ENGINE and v.get(key) is not None}
    if not cand:
        return None, None
    e = (max if mode == "max" else min)(cand, key=lambda k: cand[k][key])
    return e, cand[e][key]


def details_block(r, lines):
    lines += [f"<details><summary><code>{r['folder']}</code> &mdash; {r['version']} "
              f"&mdash; {', '.join(r['models'])}</summary>", ""]
    if r.get("settings"):
        lines += [f"config: `{r['settings']}`", ""]
    for stem in r["models"]:
        hl = r["headline"].get(stem, {})
        for fmt in MAIN_FMTS:
            per_engine = hl.get(fmt)
            if not per_engine:
                continue
            engines = [REF_ENGINE] + [e for e in per_engine if e != REF_ENGINE]
            engines = [e for e in engines if e in per_engine]
            lines += [f"#### {stem} &middot; {fmt}", "",
                      "| metric | " + " | ".join(engines) + " |",
                      "|---|" + "---:|" * len(engines)]
            rows = [
                ("prefill tok/s", [per_engine[e].get("prefill_tok_s") for e in engines], "max", 1),
                ("decode tok/s", [per_engine[e].get("decode_tok_s") for e in engines], "max", 1),
                ("TTFT ms", [per_engine[e].get("ttft_ms") for e in engines], "min", 0),
                ("ITL ms", [per_engine[e].get("itl_ms") for e in engines], "min", 1),
                ("peak RSS MB", [per_engine[e].get("rss_mb") for e in engines], "min", 0),
                ("peak GPU MB", [per_engine[e].get("gpu_mb") for e in engines], "min", 0),
                ("J/token", [per_engine[e].get("j_per_token") for e in engines], "min", 3),
                ("token match %", [per_engine[e].get("match_pct") for e in engines], "max", 1),
            ]
            for label, cells, mode, nd in rows:
                shown = []
                for c in cells:
                    if c is None:
                        shown.append("-")
                    elif nd == 0:
                        shown.append(f"{c:,.0f}")
                    elif nd == 3:
                        shown.append(f"{c:.3f}")
                    else:
                        shown.append(f"{c:,.1f}")
                lines.append("| " + label + " | " + " | ".join(shown) + " |")
            lines.append("")
        sweep = r["sweep"].get(stem) or []
        if sweep:
            lines += [f"#### {stem} &middot; bare.metal context sweep", "",
                      "| config | prompt | prefill tok/s | decode tok/s | TTFT ms | ITL ms |",
                      "|---|---:|---:|---:|---:|---:|"]
            for s in sorted(sweep, key=lambda x: (x.get("prompt_tokens") or 0, x["cfg"])):
                lines.append(f"| `{s['cfg']}` | {s.get('prompt_tokens')} | "
                             f"{f(s['prefill_tok_s'])} | {f(s['decode_tok_s'])} | "
                             f"{f(s['ttft_ms'], 0)} | {f(s['itl_ms'], 1)} |")
            lines.append("")
    lines += ["</details>", ""]
    return lines


def readme(index):
    L = [
        "# bare.metal - benchmark results",
        "",
        "Results produced by `bench/run_benchmark.sh` in",
        "[bare.metal](https://github.com/huseyincavusbi/bare.metal).",
        "",
        "Every folder under `runs/` contains `run.json` (provenance),",
        "`grand.json` (all models x engines x formats), per-model/engine slices,",
        "`summary.md`, `energy/` (trimmed powermetrics logs, previewable) and",
        "`energy-raw.tar.gz` (full raw logs).",
        "",
        "## Scoreboard",
        "",
        "| run | ver | model | fmt | bare.metal pre / dec | best pre / dec (engine) | gap |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in index["runs"]:
        for stem in r["models"]:
            for fmt in MAIN_FMTS:
                per_engine = (r["headline"].get(stem) or {}).get(fmt)
                if not per_engine:
                    continue
                ours = per_engine.get(REF_ENGINE, {})
                bpe, bp = best_engine(per_engine, "prefill_tok_s", "max")
                bde, bd = best_engine(per_engine, "decode_tok_s", "max")
                gp = ratio(bp, ours.get("prefill_tok_s"))
                gd = ratio(bd, ours.get("decode_tok_s"))
                L.append(
                    f"| [`{r['folder']}`](runs/{r['folder']}) | `{r['version']}` | {stem} | {fmt} | "
                    f"{f(ours.get('prefill_tok_s'))} / {f(ours.get('decode_tok_s'))} | "
                    f"{f(bp, 0)} ({bpe or '-'}) / {f(bd, 0)} ({bde or '-'}) | "
                    f"{'x' + f(gp, 0) if gp else '-'} / {'x' + f(gd, 0) if gd else '-'} |")
    L += ["",
          "gap = best engine / bare.metal (x1000 means the best engine is 1000x faster).",
          "Quant rows compare different quantization schemes, so token match is informational.",
          "",
          "## Progress (bare.metal, bf16)", "",
          "| run | model | prefill tok/s | decode tok/s | J/token | gap pre | gap dec |",
          "|---|---|---:|---:|---:|---:|---:|"]
    for r in index["runs"]:
        for stem in r["models"]:
            per_engine = (r["headline"].get(stem) or {}).get("bf16")
            if not per_engine:
                continue
            ours = per_engine.get(REF_ENGINE, {})
            _, bp = best_engine(per_engine, "prefill_tok_s", "max")
            _, bd = best_engine(per_engine, "decode_tok_s", "max")
            gp = ratio(bp, ours.get("prefill_tok_s"))
            gd = ratio(bd, ours.get("decode_tok_s"))
            L.append(
                f"| `{r['folder']}` | {stem} | {f(ours.get('prefill_tok_s'))} | "
                f"{f(ours.get('decode_tok_s'))} | {f(ours.get('j_per_token'), 3)} | "
                f"{'x' + f(gp, 0) if gp else '-'} | {'x' + f(gd, 0) if gd else '-'} |")
    L += ["", "## Run details", ""]
    for r in index["runs"]:
        L = details_block(r, L)
    L += ["_Auto-generated by `tools/index.py` - do not edit by hand._", ""]
    return "\n".join(L)


def main():
    index = {"schema": SCHEMA, "runs": load_runs()}
    want_index = json.dumps(index, indent=2) + "\n"
    want_readme = readme(index)
    ij, rm = os.path.join(ROOT, "index.json"), os.path.join(ROOT, "README.md")

    if "--check" in sys.argv:
        stale = []
        if not os.path.isfile(ij) or open(ij).read() != want_index:
            stale.append("index.json")
        if not os.path.isfile(rm) or open(rm).read() != want_readme:
            stale.append("README.md")
        if stale:
            print("stale: " + ", ".join(stale), file=sys.stderr)
            raise SystemExit(1)
        print("index.json and README.md are up to date")
        return

    open(ij, "w").write(want_index)
    open(rm, "w").write(want_readme)
    print(f"wrote index.json and README.md ({len(index['runs'])} runs)")


if __name__ == "__main__":
    main()
