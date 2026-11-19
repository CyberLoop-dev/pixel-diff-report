#!/usr/bin/env python3
"""Compare two local images and write a visual difference report."""
from __future__ import annotations
import argparse, html, json, shutil, sys
from pathlib import Path
from PIL import Image, ImageChops, ImageStat

def compare_images(before_path, after_path, out_dir, threshold=8):
    before=Image.open(before_path).convert("RGB")
    after=Image.open(after_path).convert("RGB")
    if before.size != after.size:
        raise ValueError(f"Image sizes differ: {before.size} vs {after.size}")
    diff=ImageChops.difference(before,after)
    pixels=list(diff.getdata())
    changed=sum(1 for pixel in pixels if max(pixel)>threshold)
    total=before.width*before.height
    mean=round(sum(ImageStat.Stat(diff).mean)/3,3)
    mask=diff.convert("L").point(lambda value:255 if value>threshold else 0)
    heat=Image.new("RGB",before.size,(18,24,38))
    red=Image.new("RGB",before.size,(255,70,110))
    heat.paste(red,mask=mask)
    overlay=Image.blend(before,after,0.5)
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    shutil.copy2(before_path,out/"before"+Path(before_path).suffix.lower())
    shutil.copy2(after_path,out/"after"+Path(after_path).suffix.lower())
    diff_path=out/"diff.png"; overlay_path=out/"overlay.png"
    heat.save(diff_path); overlay.save(overlay_path)
    report={"width":before.width,"height":before.height,"total_pixels":total,"changed_pixels":changed,
            "changed_percent":round(changed*100/total,3) if total else 0,"mean_absolute_error":mean,"threshold":threshold}
    (out/"report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    before_name="before"+Path(before_path).suffix.lower(); after_name="after"+Path(after_path).suffix.lower()
    page=f"""<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Pixel Diff Report</title>
<style>body{{font:16px system-ui;background:#0b1220;color:#e5edf7;margin:0;padding:32px}}main{{max-width:1100px;margin:auto}}h1{{color:#5eead4}}.stats,.images{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}}.card{{background:#142236;border:1px solid #29415a;border-radius:16px;padding:16px}}img{{width:100%;height:auto;border-radius:10px;background:#091423}}small{{color:#9fb0c5}}</style>
<main><h1>Pixel Diff Report</h1><div class="stats">{''.join(f'<section class="card"><small>{html.escape(k.replace("_"," ").title())}</small><h2>{html.escape(str(v))}</h2></section>' for k,v in report.items())}</div>
<div class="images">{''.join(f'<section class="card"><h3>{label}</h3><img src="{src}" alt="{label}"></section>' for label,src in [("Before",before_name),("After",after_name),("Difference heatmap","diff.png"),("50/50 overlay","overlay.png")])}</div></main></html>"""
    (out/"index.html").write_text(page,encoding="utf-8")
    return report

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("before",type=Path); ap.add_argument("after",type=Path)
    ap.add_argument("--out-dir",type=Path,default=Path("pixel-diff-report"))
    ap.add_argument("--threshold",type=int,default=8); args=ap.parse_args()
    if args.threshold<0 or args.threshold>255: ap.error("--threshold must be between 0 and 255")
    try: report=compare_images(args.before,args.after,args.out_dir,args.threshold)
    except (OSError,ValueError) as exc: print(f"error: {exc}",file=sys.stderr); return 2
    print(json.dumps(report,indent=2)); print(f"\nOpen {args.out_dir/'index.html'}")
    return 0
if __name__=="__main__": raise SystemExit(main())
