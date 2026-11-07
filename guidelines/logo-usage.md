# Primordial Weave · Logo / Mark 使用规范

> **当前状态：** 极简 Mark V1.0、标准带章 Mark V1.1 和「織」字印章 V1.1 已作为正式 PNG 在 `brand` 仓库发布（2026-11-07）。其他横向字标、深色版本、Banner、OG、头像、favicon 和 SVG 仍需单独完成或验收。

## 已批准的素材

| 图形 | 路径 | 用途 |
| --- | --- | --- |
| 极简 Mark V1.0（透明） | [2048px PNG](../exports/png/pw-mark-minimal-transparent-v1.0-2048.png) | Logo 主体、头像基础 |
| 极简 Mark V1.0（宣纸） | [2048px PNG](../exports/png/pw-mark-minimal-paper-v1.0-2048.png) | 宣纸背景展示 |
| 极简 Mark V1.0（Compact） | [2048px PNG](../exports/png/pw-mark-minimal-compact-v1.0-2048.png) | 小尺寸适配基础，favicon 仍需验收 |
| **标准 Mark V1.1（带印章）** | **[2048px PNG](../exports/png/pw-mark-standard-seal-v1.1-2048.png)** | 正式品牌组合图 |
| 印章 V1.1 | [4096px PNG](../exports/png/pw-seal-zhi-cinnabar-enlarged-v1.1-4096.png) | 唯一标准印章输入 |

## 标准 Mark V1.1 锁定构图

- 画布：2048×2048 透明 RGBA。
- 极简 Mark：1760×1760，坐标 (55,50)。
- V1.1 印章：按 Alpha 裁边后 304×304，坐标 (1480,1460)。
- 保留太极、墨环、金线、上下朱砂点与印文原始形态；只允许等比缩放、透明裁边及 Alpha 合成，不能重新生成图形。
- 印章比 V1.0 版式向左 105px、向上 117px，与外墨环保持间距。
- 标准 Mark 定稿输出 SHA-256：`1b776f96c9dcbcfe6838bd07c0d737916496e13b3e27114e4cea2da9110c1175`。

具体见 [合成规范 V1.1](MARK-COMPOSITION-SPEC.md) 和 [资产记录](../sources/logo/ASSET-RECORD.md)。在仓库根目录运行：

```bash
python3 -m pip install Pillow
python3 sources/logo/scripts/compose_mark.py
```

默认输出到 `build/standard-mark-v1.1/`，不会覆盖已批准的 `exports/png/`。

## 禁用规则

- 禁止重新生成同名的太极、印章或任意替换「織」字。
- 禁止金线周围红黄杂边、阴影、光晕、金属描边、拉伸、翻转或把太极白色区域误抠透明。
- 标准 Mark 的位置与大小已经确认；修改需另起版本并保留源文件校验记录。
- 深色背景下墨环可能失去对比度，**不得将现有版本宣传为深色优化版**。
- 小尺寸 favicon 默认不使用带印章标准版。
- PNG 不等于可编辑 SVG，SVG 工作暂缓。
- 品牌视觉定稿不代表印章获得标准小篆认证，也不代表授权第三方商用。

## 后续工作

英文与中文横向字标、README Banner、OG、Social Preview、头像、深浅色适配、单色版及 favicon 独立完成，最后核对在 `.github` 的真实显示。
