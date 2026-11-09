#!/usr/bin/env python3
"""Rebuild Primordial Weave approved seal V1.4 and centered Mark V1.2.

Usage: python3 sources/logo/scripts/compose_seal_and_mark_v1_4.py
Requires: Pillow, numpy, opencv-python-headless, cairosvg.
Only writes under build/v1.4; approved PNGs remain untouched.
"""
from __future__ import annotations
import hashlib
import io
import json
from pathlib import Path
import numpy as np
import cv2
import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'sources/logo/seal-baseplate-v1.0-1254.png'
SVG = ROOT / 'sources/logo/zhi-chongxi-approved-outline-v1.1.svg'
REFERENCE = ROOT / 'exports/png/pw-zhi-chongxi-white-transparent-v1.1-2048.png'
MARK = ROOT / 'exports/png/pw-mark-minimal-transparent-v1.0-2048.png'
OUT = ROOT / 'build/v1.4'
OUT.mkdir(parents=True, exist_ok=True)

INPUT_SHA256 = {
    BASE: '1a86d984cb2ef3e4b821b2f2a7f41a0acfd2f2b411d101050939f4daf2ea6f6f',
    SVG: '9fe81c02fd6069709a518f537542ce432a4d174c4d195b0371e9eb9569e76a81',
    REFERENCE: '17852a525e9e66b707cf2c74a29bdb36c87f8121c9f8f04e0c699975648ad877',
    MARK: 'da6ce844e3ffc8dcb27da10d610a6dbaf801f0de7003821cdd4dd06458a96863',
}
OUTPUT_SHA256 = {
    'pw-seal-zhi-chongxi-v1.4-1254.png': 'ad6003a6af85b85cb6346299dbbdbf3aa5f4f5e4c54662cb7d3d6b92c12fa85a',
    'pw-seal-zhi-chongxi-v1.4-2048.png': 'c1d4d5bc7349d5e49660a8297d7523eae4b2ca545a428d9245db384eb6f726bd',
    'pw-seal-zhi-chongxi-v1.4-4096.png': '0e00c99908e2d07cfe5d4c56fb5bd86e4c3779eb1b6b3b602c34ec8230985234',
    'pw-mark-standard-seal-v1.2-centered-2048.png': 'a0939cbd0466ab81d7a78895dc1194ac1e75035d2e4b531b268452091fa06a20',
}

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def bbox(image: Image.Image, threshold: int=16) -> tuple[int,int,int,int]:
    a = np.asarray(image.getchannel('A'))
    ys, xs = np.where(a >= threshold)
    if not len(xs):
        raise ValueError('Empty alpha channel')
    return int(xs.min()), int(ys.min()), int(xs.max())+1, int(ys.max())+1

def clean_plate() -> Image.Image:
    original = np.array(Image.open(BASE).convert('RGBA'))
    binary = np.ascontiguousarray((original[:,:,3] >= 16).astype('uint8'))
    n, labels, stats, _ = cv2.connectedComponentsWithStats(binary, 8)
    if n < 2:
        raise ValueError('No seal body found')
    main = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    selected = cv2.dilate(np.ascontiguousarray((labels==main).astype('uint8')),
                          np.ones((3,3), dtype='uint8'), iterations=1)
    original[:,:,3] = (original[:,:,3].astype('uint16') * selected).astype('uint8')
    original[original[:,:,3] == 0, :3] = 0
    return Image.fromarray(original, 'RGBA')

def render_glyph(size: int) -> Image.Image:
    raw = cairosvg.svg2png(url=str(SVG), output_width=size, output_height=size)
    return Image.open(io.BytesIO(raw)).convert('RGBA')

def make_seal(plate: Image.Image, size: int) -> Image.Image:
    canvas = plate.resize((size,size), Image.Resampling.LANCZOS)
    glyph = render_glyph(size)
    glyph = glyph.crop(bbox(glyph))
    target_h = round(size * .634)
    scale = target_h / glyph.height
    dims = (round(glyph.width*scale), target_h)
    glyph = glyph.resize(dims, Image.Resampling.LANCZOS)
    x = round(size * .50) - dims[0]//2
    y = round(size * .499) - dims[1]//2
    if not (size*.18 < x < size*.35 and y > size*.16 and x+dims[0] < size*.82 and y+dims[1] < size*.85):
        raise ValueError('Glyph overlaps border')
    white = Image.new('RGBA', glyph.size, (255,255,255,0))
    white.putalpha(glyph.getchannel('A'))
    canvas.alpha_composite(white, (x,y))
    return canvas

def make_mark(seal: Image.Image) -> Image.Image:
    canvas = Image.new('RGBA',(2048,2048),(0,0,0,0))
    mark = Image.open(MARK).convert('RGBA').resize((1760,1760), Image.Resampling.LANCZOS)
    canvas.alpha_composite(mark, (143,152))
    l,t,r,b = bbox(seal,12)
    seal = seal.crop((max(0,l-12),max(0,t-12),min(2048,r+12),min(2048,b+12)))
    scale = min(304/seal.width, 304/seal.height)
    dims = (round(seal.width*scale),round(seal.height*scale))
    seal = seal.resize(dims, Image.Resampling.LANCZOS)
    slot = Image.new('RGBA',(304,304),(0,0,0,0))
    slot.alpha_composite(seal, ((304-dims[0])//2,(304-dims[1])//2))
    canvas.alpha_composite(slot, (1482,1482))
    return canvas

def main() -> None:
    for path,expected in INPUT_SHA256.items():
        if not path.is_file() or sha(path) != expected:
            raise RuntimeError(f'Unexpected source file: {path}')
    reference = Image.open(REFERENCE).convert('RGBA')
    mask1 = np.asarray(render_glyph(2048).getchannel('A')) >= 128
    mask2 = np.asarray(reference.getchannel('A')) >= 128
    iou = float(np.logical_and(mask1,mask2).sum() / np.logical_or(mask1,mask2).sum())
    if iou < .995:
        raise RuntimeError(f'SVG/reference mismatch: IoU={iou}')
    plate = clean_plate()
    for size in (1254,2048,4096):
        target = OUT / f'pw-seal-zhi-chongxi-v1.4-{size}.png'
        make_seal(plate,size).save(target, compress_level=1)
    seal_2048 = Image.open(OUT/'pw-seal-zhi-chongxi-v1.4-2048.png').convert('RGBA')
    make_mark(seal_2048).save(OUT/'pw-mark-standard-seal-v1.2-centered-2048.png', compress_level=1)
    actual = {name:sha(OUT/name) for name in OUTPUT_SHA256}
    bad = {name:actual[name] for name,want in OUTPUT_SHA256.items() if actual[name]!=want}
    (OUT/'rebuild-report.json').write_text(json.dumps({'source_verified':True,'glyph_iou':iou,'sha256':actual,'byte_identical':not bad},indent=2)+'\n')
    if bad:
        raise RuntimeError(f'Output differs from approved exports: {bad}')
    print('All approved exports reproducible; SVG/reference IoU:', iou)

if __name__ == '__main__':
    main()
