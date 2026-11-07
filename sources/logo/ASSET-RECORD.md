# Primordial Weave · 标准 Mark 资产登记

**当前正式视觉版：V1.1（2026-11-07）**。标准 Mark 是已定稿的 **极简 Mark V1.0 + 白文「織」印章 V1.1** 的精确透明合成，不重新生图。

| 资产 | 文件与用途 | SHA-256 |
| --- | --- | --- |
| 极简透明 Mark V1.0 | [2048px PNG](../../exports/png/pw-mark-minimal-transparent-v1.0-2048.png) · 输入 | `da6ce844e3ffc8dcb27da10d610a6dbaf801f0de7003821cdd4dd06458a96863` |
| 「織」字朱砂印章 V1.1 | [4096px PNG](../../exports/png/pw-seal-zhi-cinnabar-enlarged-v1.1-4096.png) · 输入 | `a6f035646b400cc2b6b818dd6f765f8afa590b60d04fe49be2cacc3a02598368` |
| **标准 Mark V1.1** | **[2048px 透明 PNG](../../exports/png/pw-mark-standard-seal-v1.1-2048.png)** · 正式输出 | **`1b776f96c9dcbcfe6838bd07c0d737916496e13b3e27114e4cea2da9110c1175`** |

已核对 GitHub 上传文件与三文件交付 ZIP 的 Git blob 指纹及字节数；在模拟实际 `brand/` 仓库目录的本地验证中，运行 [合成脚本](scripts/compose_mark.py) 获得了与正式 PNG **完全相同的 SHA-256**。

## 锁定排版

- RGBA 透明画布：**2048×2048**。
- 极简 Mark 等比缩放为 **1760×1760**，左上角坐标 **(55,50)**。
- 印章裁除外侧透明边后缩放为 **304×304**，左上角坐标 **(1480,1460)**。
- 全部按原稿 Alpha 合成，未重新生成太极、印章或改变朱砂颜色。

## 如何复现

在仓库根目录执行：

```bash
python3 -m pip install Pillow
python3 sources/logo/scripts/compose_mark.py
```

输出默认保存在 `build/standard-mark-v1.1/`，不会覆盖 `exports/png/` 中的批准文件。详见 [合成规范 V1.1](../../guidelines/MARK-COMPOSITION-SPEC.md) · [机器记录](manifest.json)。

## 使用边界

- 该文件已获品牌方视觉确认，但**深色专用适配仍未完成**。
- 组织主页旧 Banner、OG、头像尚未同步替换。
- SVG 母版暂停，当前为可追溯 PNG 位图组合。
- 「織」字属于品牌化篆刻视觉，并未获得古文字学逐笔标准小篆认证；公开仓库不等于开放商用或再分发权。
