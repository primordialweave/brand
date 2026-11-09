# Primordial Weave · 正式 Mark V1.2 / 印章 V1.4 质量验收记录

> **2026-11-09 · 视觉定稿已确认。** 本文件记录可重复的技术检查，不表示字体许可、标准小篆逐笔认证或商标法律确认。

## 1. 最终输出及 SHA-256

| 正式文件 | 尺寸 | SHA-256 |
| --- | --- | --- |
| [印章 1254](../../exports/png/pw-seal-zhi-chongxi-v1.4-1254.png) | 1254×1254 RGBA | `ad6003a6af85b85cb6346299dbbdbf3aa5f4f5e4c54662cb7d3d6b92c12fa85a` |
| [印章 2048](../../exports/png/pw-seal-zhi-chongxi-v1.4-2048.png) | 2048×2048 RGBA | `c1d4d5bc7349d5e49660a8297d7523eae4b2ca545a428d9245db384eb6f726bd` |
| [印章 4096](../../exports/png/pw-seal-zhi-chongxi-v1.4-4096.png) | 4096×4096 RGBA | `0e00c99908e2d07cfe5d4c56fb5bd86e4c3779eb1b6b3b602c34ec8230985234` |
| [标准 Mark V1.2 居中](../../exports/png/pw-mark-standard-seal-v1.2-centered-2048.png) | 2048×2048 RGBA | `a0939cbd0466ab81d7a78895dc1194ac1e75035d2e4b531b268452091fa06a20` |

正式文件与原候选图使用相同 Git blob，旧 V1.1 图像仍保留。

## 2. 锁定输入

- 极简 Mark V1.0 SHA-256：`da6ce844e3ffc8dcb27da10d610a6dbaf801f0de7003821cdd4dd06458a96863`。
- 朱砂底板源图 SHA-256：`1a86d984cb2ef3e4b821b2f2a7f41a0acfd2f2b411d101050939f4daf2ea6f6f`。
- 已确认崇羲参考字形 SVG：`9fe81c02fd6069709a518f537542ce432a4d174c4d195b0371e9eb9569e76a81`。
- 确认白文字形参考 PNG：`17852a525e9e66b707cf2c74a29bdb36c87f8121c9f8f04e0c699975648ad877`。

## 3. 验收结论

- [x] 真透明 RGBA；尺寸正确，四角无背景。
- [x] 基于锁定母图，程序合成，不重新绘制太极。
- [x] 矢量字形与确认白文参考 PNG 的二值 Alpha 轮廓 IoU = 1.0。
- [x] 正式标准 Mark 位置：Mark (143,152)、1760×1760；印章容器 (1482,1482)、304×304。
- [x] 采用固定依赖版本、锁定输入重新构建，输出 PNG SHA-256 与 GitHub 正式文件一致。
- [x] 原 V1.1 正式资产不覆盖。
- [ ] 字体来源的授权核对及古文字学学术认证需独立办理。
- [ ] 已有 Banner/OG/Social Preview 尚未全部重做为 V1.4 印章，也没有自动替换 `.github` 主页。

## 4. 验证命令

```bash
python3 -m pip install -r sources/logo/scripts/requirements-v1.4.txt
python3 sources/logo/scripts/verify_assets_v1_4.py
python3 sources/logo/scripts/compose_seal_and_mark_v1_4.py
```

合成脚本只输出到 `build/v1.4/`，不会覆盖正式 `exports/png/`。更完整的机器读取记录见 [QA JSON](../seal/qa-v1.4.json)、[Seal Manifest](../seal/manifest-v1.4.json) 及 [Mark Manifest](manifest-v1.2-centered.json)。

**分辨率说明：** 4096px 字形由 SVG 轮廓渲染，但红色印章底板源为 1254px 位图，因此不能把该文件宣传为原生 4K 朱砂底板。
