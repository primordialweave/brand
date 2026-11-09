# Primordial Weave · 标准 Mark 资产记录

## 当前正式视觉版：V1.2 居中版（印章 V1.4）

于 2026-11-09 经品牌方确认。太极主图仍为极简 Mark V1.0，右下角使用崇羲篆体参考「織」字印章 V1.4。

| 资产 | 位置 | SHA-256 |
| --- | --- | --- |
| 极简 Mark V1.0 | [2048px PNG](../../exports/png/pw-mark-minimal-transparent-v1.0-2048.png) | `da6ce844e3ffc8dcb27da10d610a6dbaf801f0de7003821cdd4dd06458a96863` |
| 「織」字印章 V1.4 | [2048px PNG](../../exports/png/pw-seal-zhi-chongxi-v1.4-2048.png) | `c1d4d5bc7349d5e49660a8297d7523eae4b2ca545a428d9245db384eb6f726bd` |
| **标准 Mark V1.2 居中版** | **[2048px PNG](../../exports/png/pw-mark-standard-seal-v1.2-centered-2048.png)** | **`a0939cbd0466ab81d7a78895dc1194ac1e75035d2e4b531b268452091fa06a20`** |

## 已批准的精确排版

- 透明 RGBA 画布：**2048×2048**。
- 极简 Mark：1760×1760，左上角 **(143,152)**。
- 印章图层：304×304，左上角 **(1482,1482)**，透明边按 Alpha≥12 裁剪并保留 12px。
- 印章按比例适配为 **304×301**，透明容器仍为 304×304。
- 这里使用的是**居中视觉修订版**，并非早期 V1.2 草案中的“严格内侧右下齐边”。

## 复现与归档

- [精确规范 V1.2 居中版](../../guidelines/MARK-COMPOSITION-SPEC-V1.2-CENTERED.md)
- [仓库式合成脚本](scripts/compose_seal_and_mark_v1_4.py)
- [QA 记录](../seal/qa-v1.4.json) · [机器清单](manifest.json)

```bash
python3 -m pip install -r sources/logo/scripts/requirements-v1.4.txt
python3 sources/logo/scripts/compose_seal_and_mark_v1_4.py
python3 sources/logo/scripts/verify_assets_v1_4.py
```

旧正式 **V1.1** [保持原文件](../../exports/png/pw-mark-standard-seal-v1.1-2048.png)（SHA-256 `1b776f96c9dcbcfe6838bd07c0d737916496e13b3e27114e4cea2da9110c1175`）；V1.2 居中版成为新的当前正式图片，候选文件也留作历史追溯。

当前 SVG 仅包含印章字形轮廓，不构成整个 Mark 的原生矢量母版；并未替换组织 `.github` 中的旧版图片。
