# Primordial Weave · 标准 Mark 精确合成规范 V1.2（居中正式版）

> **2026-11-09 / 已获品牌方视觉确认**。本文件是 V1.2 的当前**正式实现规范**，取代此前 [V1.2 严格内侧齐边草案](MARK-COMPOSITION-SPEC-V1.2.md) 中的未批准定位方式。V1.1 仍保留历史可复现规范。

## 1. 资产锁定

- 主标：`exports/png/pw-mark-minimal-transparent-v1.0-2048.png`，SHA-256 `da6ce844e3ffc8dcb27da10d610a6dbaf801f0de7003821cdd4dd06458a96863`。
- 印章：`exports/png/pw-seal-zhi-chongxi-v1.4-2048.png`，SHA-256 `c1d4d5bc7349d5e49660a8297d7523eae4b2ca545a428d9245db384eb6f726bd`。
- 输出：`exports/png/pw-mark-standard-seal-v1.2-centered-2048.png`，SHA-256 `a0939cbd0466ab81d7a78895dc1194ac1e75035d2e4b531b268452091fa06a20`。
- **不修改**太极纹理、金线、朱砂点、印框或「織」字笔画；禁止重新生成近似图片。

## 2. 几何坐标（单位 px，左上角为 0,0）

| 图层 | 尺寸 | 坐标 |
| --- | --- | --- |
| RGBA 透明画布 | 2048×2048 | (0,0) |
| 极简 Mark | 1760×1760 | **(143,152)** |
| 「織」印章透明容器 | 304×304 | **(1482,1482)** |
| 实际印章比例缩放 | 304×301 | 在 304px 容器内居中 |

印章从 2048px 正式文件中按 Alpha ≥12 定位边界，裁边另留 12px，然后 LANCZOS 等比缩放；按 RGBA Alpha 叠加。该位置属于**视觉中心修订**，不是历史草案的“Mark Square 内侧右下角严格齐边”。两套布局不能混称。

## 3. 交付与验收

- RGBA 2048×2048、透明四角，独立印章 4096/2048/1254 PNG 同源。
- 上述文件 SHA-256 与 release manifest 完全一致；所有定稿 PNG 不覆盖旧版 V1.1。
- 使用 [可执行脚本](../sources/logo/scripts/compose_seal_and_mark_v1_4.py) 可以从锁定输入复现相同 SHA-256。
- 质量检查见 [QA 记录](../sources/seal/qa-v1.4.json)。

```bash
python3 -m pip install -r sources/logo/scripts/requirements-v1.4.txt
python3 sources/logo/scripts/compose_seal_and_mark_v1_4.py
python3 sources/logo/scripts/verify_assets_v1_4.py
```

运行结果写入 `build/v1.4/`，**不得**覆盖 `exports/png/`；仅在版本号再次升级且核验通过时改变正式组合。

## 4. 适用边界

这是品牌视觉定稿而非篆书学术认证或字体授权证明。其他横向字标、Banner、OG、Social Preview 尚未统一替换该印章；组织 `.github` 主页仍需独立发布。

历史参考：V1.1 规范在 [MARK-COMPOSITION-SPEC.md](MARK-COMPOSITION-SPEC.md)；早期 V1.2 严格齐边草案仅作设计决策历史保留。
