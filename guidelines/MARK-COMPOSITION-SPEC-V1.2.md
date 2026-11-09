# Primordial Weave · 标准 Mark 精确合成规范 V1.2（正式版）

> **版本：** V1.2 · 2026-11-09  
> **状态：** 品牌方视觉确认定稿；V1.1 历史版保留  
> **现行印章：** 崇羲参考「織」字朱砂印章 V1.4（正式 PNG）  
> **作用范围：** 标准 Mark 的居中布局、印章落款位置与可复现 PNG 合成。并不表示已获得古文字学/字体授权认证。

## 1. 版本变更

标准 Mark V1.2 使用**极简 Mark V1.0 不变母图**和**正式印章 V1.4**，经程序缩放、裁边及 Alpha 合成。V1.1 的 PNG 和原规范完整归档，不直接覆盖。

- 太极主体（含墨环、金线、朱砂点）不得重绘、拉伸或调色。
- 「織」字必须使用已确认的 SVG 字形描摹资产，不能用生成模型猜测字形。
- 印章底板保留干净朱砂红与白色内框，且外侧游离杂点已在构建中清理。
- 不叠加红框辅助线、棋盘底、白底矩形或其他装饰。

## 2. 输入与输出

| 类别 | 仓库相对路径 |
| --- | --- |
| 极简 Mark V1.0 | `exports/png/pw-mark-minimal-transparent-v1.0-2048.png` |
| 印章红底板 | `sources/logo/seal-baseplate-v1.0-1254.png` |
| 已确认参考字形 SVG | `sources/logo/zhi-chongxi-approved-outline-v1.1.svg` |
| 白文字形校验图 | `exports/png/pw-zhi-chongxi-white-transparent-v1.1-2048.png` |
| 正式印章 V1.4 | `exports/png/pw-seal-zhi-chongxi-v1.4-2048.png`（另有 1254/4096 版本） |
| **标准 Mark V1.2 正式文件** | **`exports/png/pw-mark-standard-seal-v1.2-centered-2048.png`** |
| V1.1 历史图 | `exports/png/pw-mark-standard-seal-v1.1-2048.png` |

## 3. 坐标与定位（2048×2048 RGBA）

| 图层 | 宽×高 | 左上角坐标 |
| --- | --- | --- |
| 透明画布 | 2048×2048 | (0,0) |
| 极简 Mark | 1760×1760 | **(143,152)** |
| 印章容器 | 304×304 | **(1482,1482)** |

极简 Mark 在 Alpha≥12 阈值下可见墨环包围盒经中心补齐得到 **Mark Square = (262,262,1786,1786)**。其中心为 `(1024,1024)`，与画布中心精确重合。

印章容器的右/下边缘均为 `1482 + 304 = 1786`，与 Mark Square 右/下边界严格对齐。这是 **内侧齐边方案**，不是向外跨界的另一方案。

印章的可见边缘可含飞白；以 **304×304 的定位容器**测量对齐，而非逐像素要求锯齿印泥边缘落在几何线上。

## 4. 合成细则

1. 读取母图，按 LANCZOS 等比缩放并放置于 (143,152)。
2. 对 V1.4 印章使用 Alpha≥12 的有效框，四周预留 12px，等比放入 304×304 透明容器。
3. 在 (1482,1482) 以 RGBA Alpha 合成，不使用遮罩拉伸或滤镜修改母图。
4. 输出 **2048×2048 真透明 PNG**，不在导出图层中绘制辅助线。
5. 同时校验 SHA-256、尺寸、RGBA、透明角与母图一致性。

## 5. 锁定指纹

- 现行标准 Mark PNG SHA-256：`a0939cbd0466ab81d7a78895dc1194ac1e75035d2e4b531b268452091fa06a20`
- 现行 2048px 印章 SHA-256：`c1d4d5bc7349d5e49660a8297d7523eae4b2ca545a428d9245db384eb6f726bd`
- 母图 SHA-256：`da6ce844e3ffc8dcb27da10d610a6dbaf801f0de7003821cdd4dd06458a96863`

## 6. 可重复构建

```bash
python3 -m pip install -r sources/logo/scripts/requirements-v1.4.txt
python3 sources/logo/scripts/verify_assets_v1_4.py
python3 sources/logo/scripts/compose_seal_and_mark_v1_4.py
```

重建结果仅写入 `build/v1.4/`，不会修改 `exports/png/` 中正式 PNG，且应与上面的 SHA-256 相同。见 [Logo V1.2 / Seal V1.4 QA 记录](../sources/logo/QA-V1.2-V1.4.md)。

## 7. 使用边界与历史版本

- 视觉定稿不等于字体文件许可或标准小篆字形学术认证。印章字形来自用户提供的低分辨率崇羲参考图的矢量描摹。
- 4096px 印章的字形可由 SVG 精细渲染，但其朱砂底板源为 1254px PNG 插值放大。
- `MARK-COMPOSITION-SPEC.md` 为 V1.1 历史正式规范，不能混用其 (55,50)/(1480,1460) 坐标。
- 已上传候选文件是可追溯历史记录，不是新的权威发布入口。
- GitHub 组织主页 `.github` 图像是否替换另行操作，此处仅完成 `brand` 仓库的资产版本定稿。
