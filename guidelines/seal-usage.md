# 朱砂「織」字品牌印章 · 正式使用规范 V1.4

> **当前正式视觉版本：V1.4（2026-11-09）。** V1.1、V1.0 为历史版本，保留各自文件。此确认仅涉及品牌视觉，不是古文字学认证或商用授权。

## 正式文件

| 用途 | 文件 |
| --- | --- |
| 首选主文件 | [4096px 透明 PNG](../exports/png/pw-seal-zhi-chongxi-v1.4-4096.png) |
| 常规应用/Mark 合成 | [2048px 透明 PNG](../exports/png/pw-seal-zhi-chongxi-v1.4-2048.png) |
| 原尺寸版 | [1254px 透明 PNG](../exports/png/pw-seal-zhi-chongxi-v1.4-1254.png) |

## 印章来源与技术边界

- 底板：1254×1254 朱砂红白框透明图，经连通域清理游离像素。
- 印文：根据用户确认的 144×148px 崇羲篆体参考图**描摹的 SVG 轮廓**；没有使用或分发正式字体文件。
- 色彩与结构：干净朱砂红底、白文、白色内框；禁止变色、随机重绘、替换笔画或拉伸。
- 4096px 中字形来自 SVG 渲染，底板由 1254px 位图高质量放大；不应宣称底板为原生 4K。
- 品牌图形视觉已批准，但古文字形制、字体/参考图片版权以及商用授权需单独核验。

## 使用与复现

- 官方标志的印章应采用同一个 V1.4 主文件，避免与 V1.1 混用。
- 小尺寸图标不建议使用印章；独立印章亦不替代完整组织名称。
- [资产记录](../sources/seal/ASSET-RECORD.md) · [机器清单](../sources/seal/manifest.json) · [QA](../sources/seal/qa-v1.4.json)。
- [合成脚本](../sources/logo/scripts/compose_seal_and_mark_v1_4.py) 仅向 `build/v1.4/` 写入。
- 其他 Banner / OG / Social Preview 尚未升级印章；组织主页仍需独立同步，不自动替换。

## 历史版本

- [V1.1](../sources/seal/manifest-v1.1.json)：曾获正式视觉批准，已被 V1.4 取代，但二进制文件保留。
- [V1.0](../sources/seal/manifest-v1.0.json)：历史版本。
- 后续任何字形调整都必须另起版本、保留旧稿和 SHA-256。
