#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic *programmatic* composition of Primordial Weave's 3 scenic exports, optimized V1.2.

Inputs are already approved background images, minimal Mark V1.0, approved English
wordmark V1.1, and approved seal V1.4. No text-to-image/AI generation is used.

Run from anywhere with: python3 /path/to/.../scripts/compose.py
Only writes within this package folder; never overwrites Github files.
"""
from __future__ import annotations
from PIL import Image, ImageDraw, ImageFont, ImageOps
import numpy as np
from pathlib import Path
import hashlib, json, math

ROOT=Path(__file__).resolve().parent.parent
SOURCES=ROOT/'sources'
EXPORTS=ROOT/'exports'
PREVIEWS=ROOT/'previews'
for folder in [EXPORTS,PREVIEWS]: folder.mkdir(parents=True, exist_ok=True)

PATHS={
 'bg_banner': SOURCES/'backgrounds/金线云岭水墨长卷.png',
 'bg_og': SOURCES/'backgrounds/金色织境云谷山水.png',
 'bg_social': SOURCES/'backgrounds/金线流韵山河图.png',
 'mark': SOURCES/'brand/pw-mark-minimal-transparent-v1.0-2048.png',
 'seal': SOURCES/'brand/pw-seal-zhi-chongxi-v1.4-2048.png',
 'wordmark': SOURCES/'brand/pw-wordmark-horizontal-en-v1.1-2400x600.png',
 'tagline': SOURCES/'brand/pw-tagline-ebgaramond12-exact-transparent-1200x75.png',
}
SPECS={
 'readme_banner': {
  'file':'pw-readme-banner-scenic-composed-v1.1-2400x600.png',
  'canvas':(2400,600),'bg':'bg_banner','crop_offset_y':34,
  'mark':(310,125,390),'title':(760,202,1400),
  'seal':(2180,59,106),'tagline':(790,407,1320),
  'rule_y':392,'rule_from':(988,1942),'rule_color':(176,133,72,170),
 },
 'og_share': {
  'file':'pw-og-share-scenic-composed-v1.2-1200x630.png',
  'canvas':(1200,630),'bg':'bg_og','crop_offset_y':0,
  'mark':(112,170,335),'title':(482,247,650),
  'seal':(1058,55,78),'tagline':(473,365,662),
  'rule_y':353,'rule_from':(625,998),'rule_color':(176,133,72,180),
 },
 'github_social_preview': {
  'file':'pw-github-social-preview-scenic-composed-v1.2-1280x640.png',
  'canvas':(1280,640),'bg':'bg_social','crop_offset_y':0,
  'mark':(115,165,355),'title':(495,253,700),
  'seal':(1129,55,82),'tagline':(489,370,710),
  'rule_y':361,'rule_from':(661,1040),'rule_color':(176,133,72,180),
 },
}

def sha256(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def crop_visible(im:Image.Image, threshold=12, pad=8):
    if im.mode!='RGBA': im=im.convert('RGBA')
    a=im.getchannel('A').point(lambda v:255 if v>=threshold else 0)
    box=a.getbbox()
    if box is None: raise RuntimeError('Source art is empty')
    l,t,r,b=box
    return im.crop((max(0,l-pad),max(0,t-pad),min(im.width,r+pad),min(im.height,b+pad)))

def soften_background(img:Image.Image,key:str)->Image.Image:
    """Localized low-contrast atmospheric lift. Modifies ONLY existing clean background.

    Two broad, continuous Gaussian fields brighten landscape UNDER transparent ink art
    and exact typography. Asymptotic falloff avoids box-mask seams. No AI redraw,
    no inpainting, no removal/copying of original scenic content.
    """
    if key not in ('bg_og','bg_social'):
        return img
    w,h=img.size
    yy,xx=np.mgrid[0:h,0:w].astype('float32')
    if key == 'bg_og':
        regions=[(278,348,210,155,.73),(825,377,385,116,.82)]
    else:
        regions=[(289,353,227,159,.73),(849,384,410,124,.86)]
    residual=np.ones((h,w),dtype='float32')
    for cx,cy,sx,sy,strength in regions:
        g=np.exp(-.5*(((xx-cx)/sx)**2+((yy-cy)/sy)**2))
        residual*=(1-strength*g)
    mist=np.clip(1-residual,0,.88)
    # Offset rather than flat white: preserve a gentle warm paper wash and golden lines.
    source=np.asarray(img.convert('RGB')).astype('float32')
    paper=np.array([249.,238.,221.],dtype='float32')
    # Apply perceptual lift mostly where source is dark. Prevent flattening of highlights.
    luminosity=(.2126*source[:,:,0]+.7152*source[:,:,1]+.0722*source[:,:,2])
    darkness=np.clip((252-luminosity)/130.,.20,1.)
    weight=mist*darkness*.94
    merged=source*(1-weight[:,:,None])+paper[None,None,:]*weight[:,:,None]
    return Image.fromarray(np.uint8(np.clip(merged+0.5,0,255)),'RGB').convert('RGBA')

def background(key:str,size,crop_offset_y=0):
    src=Image.open(PATHS[key]).convert('RGB')
    tw,th=size
    # Integer crop in ORIGINAL pixels, then LANCZOS. The original is kept untouched.
    target_ratio=tw/th
    sw,sh=src.size
    if sw/sh < target_ratio:
        keep_h=int(round(sw/target_ratio))
        top=min(max(0,int(crop_offset_y)),sh-keep_h)
        region=(0,top,sw,top+keep_h)
    else:
        keep_w=int(round(sh*target_ratio))
        left=(sw-keep_w)//2
        region=(left,0,left+keep_w,sh)
    resized=src.crop(region).resize(size,Image.Resampling.LANCZOS).convert('RGBA')
    return soften_background(resized,key),region

def paste_fit(base, art, x,y, target_width):
    out_w=int(target_width)
    out_h=int(round(art.height*out_w/art.width))
    art=art.resize((out_w,out_h),Image.Resampling.LANCZOS)
    if x<0 or y<0 or x+out_w>base.width or y+out_h>base.height:
        raise ValueError(f'Layer out of bounds: {(x,y,out_w,out_h)} / {base.size}')
    base.alpha_composite(art,(x,y))
    return [int(x),int(y),int(x+out_w),int(y+out_h)]

def build():
    missing=[str(p) for p in PATHS.values() if not p.is_file()]
    if missing:raise FileNotFoundError('Missing approved source files: '+', '.join(missing))
    mark=crop_visible(Image.open(PATHS['mark']).convert('RGBA'),12,10)
    seal=crop_visible(Image.open(PATHS['seal']).convert('RGBA'),12,7)
    wmk=Image.open(PATHS['wordmark']).convert('RGBA')
    # The previously approved English wordmark is a lockup with minimal Mark on left.
    # The text artwork starts after x=750. Crop the *actual wordmark pixels* (not OCR,
    # fresh font rendering, or simulated typography). This prevents duplicating the mark.
    title=crop_visible(wmk.crop((750,0,wmk.width,wmk.height)),12,10)
    tagline=crop_visible(Image.open(PATHS['tagline']).convert('RGBA'),2,2)
    manifest={
      'title':'Primordial Weave scenic composites · PROGRAMMATIC v1.2',
      'method':'Pillow only; input is three background plates + exact pre-approved assets. No generative image tool used.',
      'source_sha256':{k:sha256(v) for k,v in PATHS.items()},
      'source_canvas':{k:Image.open(v).size for k,v in PATHS.items()},
      'out':{},
    }
    previews=[]
    for key,spec in SPECS.items():
        canvas, crop_region=background(spec['bg'],spec['canvas'],spec['crop_offset_y'])
        mw=spec['mark'][2]; mx,my=spec['mark'][:2]
        box_mark=paste_fit(canvas,mark,mx,my,mw)
        tx,ty,tw=spec['title']
        box_title=paste_fit(canvas,title,tx,ty,tw)
        sx,sy,sw=spec['seal']
        box_seal=paste_fit(canvas,seal,sx,sy,sw)
        # Thin gold rule is separate vector-like layer drawn with Pillow.
        draw=ImageDraw.Draw(canvas,'RGBA')
        rx1,rx2=spec['rule_from']
        ry=spec['rule_y']
        draw.line((rx1,ry,rx2,ry),fill=spec['rule_color'],width=2 if key=='readme_banner' else 1)
        lx,ly,lw=spec['tagline']
        box_tagline=paste_fit(canvas,tagline,lx,ly,lw)
        # ensure none of the brand layers cross (rule may be adjacent but not part of asset masks)
        for a,b in [(box_mark,box_title),(box_mark,box_seal),(box_title,box_seal),(box_title,box_tagline),(box_tagline,box_seal)]:
            inter_w=max(0,min(a[2],b[2])-max(a[0],b[0]))
            inter_h=max(0,min(a[3],b[3])-max(a[1],b[1]))
            if inter_w*inter_h>0:raise ValueError(f'Layer bounding rectangles overlap in {key}: {a},{b}')
        out=EXPORTS/spec['file']
        canvas.convert('RGB').save(out,format='PNG',optimize=True)
        if key=='github_social_preview':
            # Safe 1-MB social delivery; preserve RGB PNG as lossless master.
            social_jpeg=EXPORTS/'pw-github-social-preview-scenic-composed-v1.2-1280x640-github.jpg'
            canvas.convert('RGB').save(social_jpeg,format='JPEG',quality=91,subsampling=0,optimize=True,progressive=True)
            if social_jpeg.stat().st_size>=1_000_000:
                raise ValueError('Social Preview JPEG exceeds 1MB')
            # Optional Indexed PNG derivative for upload while retaining master RGB PNG.
            optimized_png=EXPORTS/'pw-github-social-preview-scenic-composed-v1.2-1280x640-github-optimized.png'
            pal=canvas.convert('RGB').quantize(colors=256,method=Image.Quantize.MEDIANCUT,
                      dither=Image.Dither.FLOYDSTEINBERG)
            pal.save(optimized_png,format='PNG',optimize=True,compress_level=9)
            if optimized_png.stat().st_size>=1_000_000:
                raise ValueError('Social Preview optimized PNG exceeds 1MB')
        # preview at target size + optionally small-scale thumbnail for GitHub/social legibility
        down_width=1000 if spec['canvas'][0]>1600 else 800
        thumb=canvas.convert('RGB').resize((down_width,int(round(spec['canvas'][1]*down_width/spec['canvas'][0]))),Image.Resampling.LANCZOS)
        thumb.save(PREVIEWS/(key+'-small.jpg'),quality=93)
        previews.append((key,thumb))
        manifest['out'][key]={
          'filename':out.name,'size':spec['canvas'],'sha256':sha256(out),
          'source_background':spec['bg'],'background_crop_original_pixels':crop_region,
          'layer_boxes':{'mark':box_mark,'wordmark_text':box_title,'seal':box_seal,'tagline':box_tagline},
          'logo_reconstruction':'Exact resized transparent source artwork; no AI redraw.',
          'background_optimization':key in ['og_share','github_social_preview'],
          'social_jpeg': 'pw-github-social-preview-scenic-composed-v1.2-1280x640-github.jpg' if key=='github_social_preview' else None,
          'social_optimized_png':'pw-github-social-preview-scenic-composed-v1.2-1280x640-github-optimized.png' if key=='github_social_preview' else None
        }
    # comparison contactsheet (background neutral, no extra images generated)
    tile_w=1140
    imgs=[]
    for key,_ in previews:
        orig=Image.open(EXPORTS/SPECS[key]['file']).convert('RGB')
        size=(tile_w,round(orig.height*tile_w/orig.width))
        imgs.append((key,orig.resize(size,Image.Resampling.LANCZOS)))
    canvas=Image.new('RGB',(tile_w+80,sum(im.height+84 for _,im in imgs)+48),'#f4f1ea')
    d=ImageDraw.Draw(canvas)
    try:
        ft=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',22)
    except OSError:
        ft=ImageFont.load_default()
    yy=20
    for name,im in imgs:
        d.text((40,yy),name.replace('_',' ').upper(),fill='#333333',font=ft)
        yy+=36
        canvas.paste(im,(40,yy)); yy+=im.height+48
    canvas.crop((0,0,canvas.width,yy)).save(PREVIEWS/'three-asset-comparison.jpg',quality=92)
    (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return manifest

if __name__=='__main__':
    m=build()
    for key,v in m['out'].items():print(key,v['size'],v['sha256'][:16],v['layer_boxes'])
