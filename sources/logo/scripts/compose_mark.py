#!/usr/bin/env python3
"""Primordial Weave 标准 Mark：仅精确合成现有 PNG，不生成新的图形。"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageChops

CANVAS = (2048, 2048)
MARK_RESIZED = (1760, 1760)
MARK_POSITION = (55, 50)
SEAL_VISIBLE_SIZE = (304, 304)
SEAL_POSITION = (1480, 1460)  # V1.1: left 105px, up 117px vs V1.0
SEAL_CROP_ALPHA_THRESHOLD = 12
SEAL_CROP_PADDING = 12

MARK_SHA256 = "da6ce844e3ffc8dcb27da10d610a6dbaf801f0de7003821cdd4dd06458a96863"
SEAL_SHA256 = "a6f035646b400cc2b6b818dd6f765f8afa590b60d04fe49be2cacc3a02598368"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as f:
        while chunk := f.read(1024*1024):
            digest.update(chunk)
    return digest.hexdigest()


def crop_source_seal(image: Image.Image) -> tuple[Image.Image, tuple[int,int,int,int]]:
    """只去掉四周多余透明画布，不修改印章内部笔触或 RGB 值。"""
    # Alpha 中微量暗影噪声不影响边界估计，原始透明像素不做颜色更改。
    mask = image.getchannel('A').point(lambda a: 255 if a > SEAL_CROP_ALPHA_THRESHOLD else 0)
    box = mask.getbbox()
    if box is None:
        raise ValueError('印章 Alpha 全透明，不能合成')
    p = SEAL_CROP_PADDING
    box = (max(0,box[0]-p), max(0,box[1]-p),
           min(image.width,box[2]+p), min(image.height,box[3]+p))
    return image.crop(box), box


def create_mark(mark_path: Path, seal_path: Path, output_dir: Path, strict=True):
    observed = {'mark_sha256':sha256(mark_path),'seal_sha256':sha256(seal_path)}
    if strict:
        for label,expected in [('mark',MARK_SHA256),('seal',SEAL_SHA256)]:
            if observed[label+'_sha256'] != expected:
                raise ValueError(f'{label} SHA-256 与锁定母版不一致；禁止悄悄换用旧图')

    mark=Image.open(mark_path).convert('RGBA')
    seal=Image.open(seal_path).convert('RGBA')
    if mark.size != (2048,2048) or seal.size != (4096,4096):
        raise ValueError(f'不符合锁定的原始尺寸，mark={mark.size}, seal={seal.size}')
    mark=mark.resize(MARK_RESIZED,Image.Resampling.LANCZOS)
    seal,crop_box=crop_source_seal(seal)
    seal=seal.resize(SEAL_VISIBLE_SIZE,Image.Resampling.LANCZOS)
    # 两张独立图层用于无重叠检测
    mark_layer=Image.new('RGBA',CANVAS,(0,0,0,0))
    seal_layer=Image.new('RGBA',CANVAS,(0,0,0,0))
    mark_layer.alpha_composite(mark,MARK_POSITION)
    seal_layer.alpha_composite(seal,SEAL_POSITION)
    mark_binary = mark_layer.getchannel('A').point(lambda x:255 if x>20 else 0)
    seal_binary = seal_layer.getchannel('A').point(lambda x:255 if x>20 else 0)
    overlap = ImageChops.darker(mark_binary,seal_binary).getbbox()
    if overlap is not None:
        raise ValueError(f'主体与印章在 alpha>20 的区域发生碰撞，重叠边界={overlap}')

    canvas=Image.new('RGBA',CANVAS,(0,0,0,0))
    canvas.alpha_composite(mark_layer)
    canvas.alpha_composite(seal_layer)
    assert canvas.getpixel((0,0))[3] == 0
    assert canvas.getpixel((2047,2047))[3] == 0
    assert canvas.getpixel((730,650))[3] >= 250, '太极白色区域的 Alpha 不应被删除'

    output_dir.mkdir(parents=True,exist_ok=True)
    file=output_dir/'pw-mark-standard-seal-v1.1-2048.png'
    canvas.save(file,optimize=True)
    # 浅色/深色只是验收预览，不作为正式品牌独立变体。
    for rgb,stem in [((248,244,236),'light'),((28,29,31),'dark')]:
        bg=Image.new('RGBA',CANVAS,(*rgb,255))
        bg.alpha_composite(canvas)
        bg.convert('RGB').resize((800,800),Image.Resampling.LANCZOS).save(output_dir/f'proof-{stem}-800.jpg',quality=94)
    result={
      'status':'visual-approved-layout-v1.1',
      'layout_version':'1.1', 'reference_layout_version':'1.0',
      'previous_seal_position':[1585,1577],
      'offset_from_v1_0':[-105,-117],
      'input_hashes':observed,
      'canvas':list(CANVAS),'mark_resized':list(MARK_RESIZED),'mark_position':list(MARK_POSITION),
      'seal_crop_bbox_source_px':list(crop_box),'seal_size':list(SEAL_VISIBLE_SIZE),
      'seal_position':list(SEAL_POSITION),'pixel_bbox_alpha_nonzero':list(canvas.getchannel('A').getbbox()),
      'overlap_alpha_gt20':False,'paper_background_baked_in':False,
      'seal_identity':'exact V1.1 input PNG; no generated/repainted glyph',
      'output_png_sha256':sha256(file),
      'note':'PNG 只经 RGBA 拉伸与 alpha_composite；不是图像模型重绘。深色专用版未批准。'
    }
    (output_dir/'QA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    print('Wrote',file)


def main():
    home=Path(__file__).resolve().parents[3]
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mark',type=Path,default=home/'exports/png/pw-mark-minimal-transparent-v1.0-2048.png')
    p.add_argument('--seal',type=Path,default=home/'exports/png/pw-seal-zhi-cinnabar-enlarged-v1.1-4096.png')
    p.add_argument('--out-dir',type=Path,default=home/'build/standard-mark-v1.1')
    p.add_argument('--skip-hash-check',action='store_true',help='仅在明确重建新版本时使用，正式出图不要开启')
    a=p.parse_args()
    create_mark(a.mark,a.seal,a.out_dir,strict=not a.skip_hash_check)

if __name__=='__main__':
    main()
