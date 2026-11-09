# Primordial Weave · 标准 Mark 资产登记

**当前正式版：V1.2（居中，搭配 V1.4 印章） · 2026-11-09。** 已通过品牌方视觉确认及本地重复构建 SHA-256 核验；V1.1 保留为历史已批准版本。

| 资产 | 正式路径 | SHA-256 |
| --- | --- | --- |
| 极简 Mark V1.0（锁定母图） | [2048px PNG](../../exports/png/pw-mark-minimal-transparent-v1.0-2048.png) | `da6ce844e3ffc8dcb27da10d610a6dbaf801f0de7003821cdd4dd06458a96863` |
| 「織」字印章 V1.4 | [2048px PNG](../../exports/png/pw-seal-zhi-chongxi-v1.4-2048.png) | `c1d4d5bc7349d5e49660a8297d7523eae4b2ca545a428d9245db384eb6f726bd` |
| **标准 Mark V1.2** | **[2048px 透明 PNG](../../exports/png/pw-mark-standard-seal-v1.2-centered-2048.png)** | **`a0939cbd0466ab81d7a78895dc1194ac1e75035d2e4b531b268452091fa06a20`** |
| 历史标准 Mark V1.1 | [2048px PNG](../../exports/png/pw-mark-standard-seal-v1.1-2048.png) | `a0939cbd0466ab81d7a78895dc1194ac1e75035d2e4b531b268452091fa06a20` |

## 锁定构图

- 画布：2048×2048 透明 RGBA。
- 极简 Mark V1.0 缩放至 1760×1760，左上角 **(143,152)**。
- 印章 V1.4 等比适配 304×304 容器，左上角 **(1482,1482)**。
- Mark Square = **(262,262,1786,1786)**，几何中心为 (1024,1024)，与画布中心相同。
- 印章容器右/下边缘与 Mark Square 右/下边缘相等。
- 未重绘母图或印文；沿用 Alpha 裁剪、等比缩放与合成。

详见 [现行精确合成规范](../../guidelines/MARK-COMPOSITION-SPEC-V1.2.md)、[QA 检查](QA-V1.2-V1.4.md)、[复现脚本](scripts/compose_seal_and_mark_v1_4.py)。当前输入印章源为参考图描摹，不视作字形专业认证；官方 `.github` 宣传素材尚未自动替换。
