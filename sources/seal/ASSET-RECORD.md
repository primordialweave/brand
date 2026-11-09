# Primordial Weave · 「織」字朱砂印章资产记录

## 当前正式版：V1.4（2026-11-09）

品牌方确认这版视觉定稿。字形为根据已提供的崇羲篆体参考图片描摹并核对的矢量轮廓；**不是实际加载崇羲字体文件，也不代表字形已获得古文字学认证**。

| 正式文件 | 尺寸 | SHA-256 |
| --- | --- | --- |
| [pw-seal-zhi-chongxi-v1.4-1254.png](../../exports/png/pw-seal-zhi-chongxi-v1.4-1254.png) | 1254×1254 | `ad6003a6af85b85cb6346299dbbdbf3aa5f4f5e4c54662cb7d3d6b92c12fa85a` |
| [pw-seal-zhi-chongxi-v1.4-2048.png](../../exports/png/pw-seal-zhi-chongxi-v1.4-2048.png) | 2048×2048 | `c1d4d5bc7349d5e49660a8297d7523eae4b2ca545a428d9245db384eb6f726bd` |
| [pw-seal-zhi-chongxi-v1.4-4096.png](../../exports/png/pw-seal-zhi-chongxi-v1.4-4096.png) | 4096×4096 | `0e00c99908e2d07cfe5d4c56fb5bd86e4c3779eb1b6b3b602c34ec8230985234` |

**推荐主文件**：4096px 透明 PNG；2048px 为通用合成输入，1254px 为源尺寸导出。4096px 采用 SVG 渲染文字、1254px 底板插值缩放，不是原生 4K 底板。

## 锁定来源与复现

- 无字朱砂底板：`sources/logo/seal-baseplate-v1.0-1254.png`，SHA-256 `1a86d984cb2ef3e4b821b2f2a7f41a0acfd2f2b411d101050939f4daf2ea6f6f`。
- 「織」字轮廓：`sources/logo/zhi-chongxi-approved-outline-v1.1.svg`，SHA-256 `9fe81c02fd6069709a518f537542ce432a4d174c4d195b0371e9eb9569e76a81`。
- [可执行合成脚本](../logo/scripts/compose_seal_and_mark_v1_4.py) · [QA 报告](qa-v1.4.json) · [Manifest](manifest.json)。

在仓库根目录执行：

```bash
python3 -m pip install -r sources/logo/scripts/requirements-v1.4.txt
python3 sources/logo/scripts/compose_seal_and_mark_v1_4.py
python3 sources/logo/scripts/verify_assets_v1_4.py
```

重建输出位于 `build/v1.4/`，不会覆盖已经定稿的 `exports/png/`。

## 历史与使用边界

- V1.1 的三个 PNG 与 [历史 Manifest](manifest-v1.1.json) 保留，不再是当前推荐资产。
- 先前带 `candidate` 后缀的 V1.4 文件保留作追溯；正式引用应使用无候选后缀文件。
- 品牌视觉确认不等于字体来源授权、古文字学逐笔认证或向公众授予商用/再分发许可。
- README Banner、OG、Social Preview 等旧素材尚未统一替换新印章；本次只发布印章与标准 Mark 的正式版本。
