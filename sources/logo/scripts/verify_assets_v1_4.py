#!/usr/bin/env python3
"""Verify released V1.4 seal and centered V1.2 Mark in the brand repository."""
import hashlib, json
from pathlib import Path
import numpy as np
import cv2
from PIL import Image

ROOT=Path(__file__).resolve().parents[3]
PNG=ROOT/'exports/png'
ITEMS={
 'pw-seal-zhi-chongxi-v1.4-1254.png':(1254,'ad6003a6af85b85cb6346299dbbdbf3aa5f4f5e4c54662cb7d3d6b92c12fa85a'),
 'pw-seal-zhi-chongxi-v1.4-2048.png':(2048,'c1d4d5bc7349d5e49660a8297d7523eae4b2ca545a428d9245db384eb6f726bd'),
 'pw-seal-zhi-chongxi-v1.4-4096.png':(4096,'0e00c99908e2d07cfe5d4c56fb5bd86e4c3779eb1b6b3b602c34ec8230985234'),
 'pw-mark-standard-seal-v1.2-centered-2048.png':(2048,'a0939cbd0466ab81d7a78895dc1194ac1e75035d2e4b531b268452091fa06a20')
}
def main():
    results={}
    for name,(size,expected) in ITEMS.items():
        path=PNG/name
        if not path.exists(): raise FileNotFoundError(path)
        digest=hashlib.sha256(path.read_bytes()).hexdigest()
        im=Image.open(path).convert('RGBA')
        if digest != expected or im.size != (size,size):
            raise ValueError(f'Checksum/dimension mismatch: {name}')
        alpha=np.asarray(im.getchannel('A'))
        if any(int(alpha[y,x])>0 for x,y in [(0,0),(0,size-1),(size-1,0),(size-1,size-1)]):
            raise ValueError(f'Nontransparent corner: {name}')
        n,_,_,_=cv2.connectedComponentsWithStats(np.ascontiguousarray((alpha>=16).astype('uint8')),8)
        if n<2: raise ValueError(f'No visible art: {name}')
        results[name]={'px':[size,size],'format':'RGBA PNG','sha256':digest,'visible_alpha_components':n-1,'pass':True}
    print(json.dumps({'ok':True,'files':results},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
