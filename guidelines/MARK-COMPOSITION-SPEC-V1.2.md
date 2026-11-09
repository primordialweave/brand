# Primordial Weave · 标准 Mark 精确合成规范 V1.2

> **文档编号：** PW-BRAND-STD-MARK-001  
> **版本：** V1.2 · 2026-11-08  
> **状态：** **版式规范候选，待按本规范输出 PNG 并完成视觉验收**  
> **推荐仓库路径：** `guidelines/MARK-COMPOSITION-SPEC-V1.2.md`  
> **版本关系：** V1.1 已批准并归档；V1.2 为拟议的新排版规则，**在出图验收前不得替代 V1.1 正式 PNG**。

## 1. 目的和本次变更范围

本次只重新定义右下角 **「織」字朱砂印章** 相对极简 Mark 的位置：从 V1.1 的固定绝对坐标，改为以极简 Mark **最外层水墨圆环的外接正方形**（下称 **Mark Square**）右下角定位。

以下资产和设计元素必须保持不变：

- 已定稿极简 Mark V1.0：黑白太极、双鱼眼、外围水墨圆环、金色细环、上下朱砂点及纹理。
- 已定稿正式「織」字白文朱砂印章 V1.1：字形、印框、印泥质感和颜色。
- 输出画布尺寸、图层缩放方法、透明背景及颜色处理。
- 只做**读取现有 PNG → 等比缩放 → 按坐标合成**，禁止使用生成模型重新绘制或猜测笔画。

## 2. 输入与输出资产

| 角色 | 规范文件（相对 `brand/` 仓库根目录） | 要求 |
| --- | --- | --- |
| 主 Mark | `exports/png/pw-mark-minimal-transparent-v1.0-2048.png` | 已批准，2048 × 2048，RGBA |
| 正式印章 | `exports/png/pw-seal-zhi-cinnabar-enlarged-v1.1-4096.png` | 已批准，白文朱砂，RGBA |
| V1.1 对照图 | `exports/png/pw-mark-standard-seal-v1.1-2048.png` | 只作版本比较，不作为新合成输入 |
| **V1.2 目标输出** | `exports/png/pw-mark-standard-seal-v1.2-2048.png` | **2048 × 2048、RGBA、真透明** |

**禁止修改或覆盖**上述原始 PNG。V1.2 未验收时，先输出到 `build/standard-mark-v1.2/`；验收通过后再复制至 `exports/png/`。

## 3. 画布和锁定主图参数

以左上角为 `(0, 0)`，X 向右、Y 向下，单位为像素：

| 图层 | 尺寸 | 左上角坐标 | 说明 |
| --- | --- | --- | --- |
| 透明画布 | 2048 × 2048 | `(0, 0)` | 不含底色 |
| 极简 Mark | 1760 × 1760 | `(55, 50)` | **完全沿用 V1.1** |
| 正式印章 | 304 × 304 | **由 Mark Square 动态计算** | **沿用 V1.1 尺寸，只调整位置** |

主 Mark 的缩放方式统一使用高质量、保持长宽比的重采样；若重新构建时需字节级复现，应与正式合成脚本使用相同的 Pillow 版本与参数。

## 4. Mark Square 的唯一定位口径

**Mark Square** 指上述主 Mark 图层在画布上显示后，**最外层水墨圆环**的可见轮廓所对应的外接正方形；不包含印章，也不允许把透明画布的 2048 × 2048 全幅误作 Mark Square。

### 4.1 基准生成步骤

1. 读取正式极简 Mark V1.0 PNG，并按 §3 放置到透明画布。
2. 计算主 Mark 图层的有效 Alpha 边界，采用 **Alpha ≥ 12/255** 作为默认可见阈值，以避免几乎透明的单像素噪点造成边界漂移。
3. 得到矩形 `(L, T, R, B)`，其中 `R`、`B` 为**不含端点的右、下边界**。
4. 设 `S = max(R-L, B-T)`，以该矩形中心为中心构建正方形。最终使用整数坐标 `(square_left, square_top, square_right, square_bottom)`，即 **Mark Square**。
5. **固定并记录**计算结果、阈值、来源 SHA-256 及 Pillow 版本。发布后的同一 V1.2 文件不得因二次自动检测而改变坐标。

> 如母图包含与外圈不相连的透明抗锯齿残留，必须先人工检查有效边界，避免将异常噪点算作主体。**不允许为迁就印章位置而修改母图像素。**

### 4.2 本版定位公式（严格边缘对齐）

设经过透明裁边和等比缩放的印章图层尺寸为 `seal_size = 304`。则：

```python
seal_x = square_right  - seal_size
seal_y = square_bottom - seal_size
```

因此必须满足：

```text
印章外框右边缘 = Mark Square 的右边缘
印章外框下边缘 = Mark Square 的下边缘
```

这是一种**位于 Mark Square 内侧的右下角齐边版式**。红色辅助线、外接框和角标框仅用于检查，**不得出现在交付 PNG 中**。

**设计歧义说明：** 用户原始标注图的印章可见轮廓看起来略微跨过红色大正方形右/下边界；那属于“角部跨界落款”，不同于上述“严格内侧齐边”公式。本 V1.2 文档以此前确认的**严格右、下边缘对齐**文字规范为准。若最终希望印章像参考截图那样向外越界，必须在出图验收时改为明示的“跨界版式”并记录偏移量，不可悄悄混用两套坐标。

## 5. 印章前处理（保持 V1.1 规范）

- 读取 `pw-seal-zhi-cinnabar-enlarged-v1.1-4096.png`。
- 裁剪以 **Alpha ≥ 12** 计算的有效包围盒，向外保留 **12px 原始像素**缓冲区，不能剪掉印框飞白和边缘细节。
- 等比例缩放至适配的 **304 × 304** 图层；若源裁边后宽高不完全相同，先在透明正方形容器内居中，**禁止拉伸印章**。
- 不改变红色印泥、白文字形、印框形态，也不添加描边、光晕、投影、锐化滤镜或背景色。

## 6. 合成与安全限制

1. 使用 RGBA Alpha 合成，确保图层外区域完全透明。
2. 主图与印章在合成前均保留独立透明通道；合成时不使用 JPEG 或白色底图。
3. 允许“贴角落款”的结构关系，但**不得遮挡阴阳鱼主体、两枚鱼眼及两枚朱砂点**，不得破坏主体可读性。
4. 如果严格内侧齐边导致印章覆盖水墨圆环的关键笔触、产生明显碰撞或使组合重心失衡，应**先标记视觉验收未通过**，不得擅自移动坐标或宣称已定稿。
5. 印章不允许机械挤到画板边缘之外；应有画布安全留白。
6. 检查金线周边是否出现新增红/黄脏边。不得通过重画太极或印章来修复。

### 6.1 微调原则

仅在视觉验收阶段，允许基于公式结果在水平/垂直方向各 **±3px**（约为印章尺寸的 1%）进行微调；如使用了微调，必须在规范及 QA 报告中明确记录最终坐标，不再声称两条边与 Mark Square 严格像素齐平。超过 ±3px 应形成新候选，不得静默覆盖。

## 7. 参考实现伪代码

```python
from PIL import Image

CANVAS = (2048, 2048)
MARK_SIZE = (1760, 1760)
MARK_POS = (55, 50)
SEAL_SIZE = 304

canvas = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
mark = Image.open(MARK_PATH).convert("RGBA")
mark = mark.resize(MARK_SIZE, Image.Resampling.LANCZOS)
canvas.alpha_composite(mark, MARK_POS)

# 在尚未叠加印章前，按 §4 的阈值规则，从主 Mark 图层求 Mark Square。
# 下列坐标须由检测结果得出、经人工检查，并在发布时固定记录。
square_left, square_top, square_right, square_bottom = detect_mark_square(
    mark, mark_origin=MARK_POS, alpha_threshold=12
)

seal = load_and_prepare_approved_seal(
    SEAL_PATH, size=SEAL_SIZE, alpha_threshold=12, padding=12
)
seal_x = square_right - SEAL_SIZE
seal_y = square_bottom - SEAL_SIZE
canvas.alpha_composite(seal, (seal_x, seal_y))

# 预发布请写入 build/；验收后再将 PNG 提交到 exports/png/。
canvas.save(OUTPUT_PATH)
```

**注意：** `detect_mark_square()`、`load_and_prepare_approved_seal()` 代表 §4–§5 中的明确规则，以上为流程示意，**不是可直接运行的完整脚本**。正式实施时应在 `sources/logo/scripts/compose_mark.py` 的新 V1.2 分支或独立脚本中实现这两项函数，并补充哈希及碰撞检查。

## 8. 验收检查表

- [ ] 主 Mark 与正式 V1.0 文件一致，仅按锁定尺寸缩放、放置，未重新生成。
- [ ] 印章与正式 V1.1 文件一致，仅裁透明边、等比缩放，未重新生成。
- [ ] 输出为 2048 × 2048 RGBA PNG，四角和外围背景真透明。
- [ ] 根据单独记录的 Alpha 阈值计算并固定 Mark Square，附计算结果。
- [ ] 标注框检查：印章右边与 Mark Square 右边对齐，印章底边与 Mark Square 底边对齐（若有微调须单列）。
- [ ] 印章不遮挡太极主体、鱼眼及朱砂点；外围墨环与印章关系清楚。
- [ ] 无新增红黄彩边、白边、伪透明底或错误的字形。
- [ ] 输出浅色/深色背景预览，以及 V1.1/V1.2 同画布版式对照。
- [ ] 视觉负责人确认最终布局，明确选择“严格齐边”还是另行提出“角部跨界”。
- [ ] 记录输入/输出文件 SHA-256 和最终绝对坐标，并更新资产清单。

## 9. 版本管理与归档

| 版本 | 状态 | 版式差异 |
| --- | --- | --- |
| **V1.1** | 已批准、保留 | 印章 304 × 304，左上角 `(1480, 1460)`；固定绝对坐标 |
| **V1.2** | 待生成与视觉验收 | 印章尺寸不变，改按 Mark Square 右下角定位 |

建议归档：

```text
brand/
├── guidelines/
│   ├── MARK-COMPOSITION-SPEC.md            # 当前已批准 V1.1 规范（暂保留）
│   └── MARK-COMPOSITION-SPEC-V1.2.md       # 本文件，待验收
├── sources/logo/scripts/
│   └── compose_mark.py                    # 后续增加 V1.2 支持
├── exports/png/
│   └── pw-mark-standard-seal-v1.1-2048.png # 现行正式版本，不覆盖
└── build/standard-mark-v1.2/               # 新版候选：不提交正式 exports
```

验收完成后，可新增：

- `exports/png/pw-mark-standard-seal-v1.2-2048.png`
- `references/pw-mark-standard-seal-v1.2-proof-light.png`
- `references/pw-mark-standard-seal-v1.2-proof-dark.png`
- `references/pw-mark-standard-seal-v1.1-v1.2-comparison.png`

同时更新 `sources/logo/ASSET-RECORD.md`、`sources/logo/manifest.json`、`CHANGELOG.md`、`PLAN.md` 和 Logo 使用规范。**在新 PNG 被认可之前，V1.1 仍是现行标准。**
