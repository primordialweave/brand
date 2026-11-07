# Primordial Weave · 原初织界品牌规范

<p align="center">
  <strong>灵感源自古老智慧，创造面向开放未来的工具。</strong>
</p>

<p align="center">
  <a href="./README.md">English</a> · <a href="./README.zh-CN.md">简体中文</a>
</p>

**Primordial Weave（原初织界）** 是以中国传统哲学、水墨审美和现代开源精神为灵感的品牌。

> **当前状态（2026-11-07）：** 极简 Mark V1.0、标准 Mark V1.1（带「織」字朱砂印章）与独立印章 V1.1 的 PNG 均已上传。标准 Mark 已获视觉确认，合成规范及脚本已能在真实仓库目录下复现完全一致的正式 PNG。组织 `.github` 主页旧 Banner、OG 与头像仍未替换；SVG、深色专用版及素材授权是独立待办。

## 文档导航

| 内容 | 文件 |
| --- | --- |
| 品牌定位、理念、视觉原则 | [品牌规范](guidelines/brand-guidelines.md) |
| 标志和太极使用 | [Logo 使用规范](guidelines/logo-usage.md) · [标准 Mark 合成规范 V1.1](guidelines/MARK-COMPOSITION-SPEC.md) · [Mark 资产登记](sources/logo/ASSET-RECORD.md) |
| 正式印章 V1.1 与文化考证边界 | [印章使用规范](guidelines/seal-usage.md) · [资产记录](sources/seal/ASSET-RECORD.md) |
| 中英文字体与字号建议 | [字体规范](guidelines/typography.md) |
| 著作权、字体及开源许可边界 | [授权说明](guidelines/licensing.md) |
| 候选标准色值 | [colors.json](design-tokens/colors.json) |
| 候选字体 Token | [typography.json](design-tokens/typography.json) |
| 阶段执行计划 | [PLAN.md](PLAN.md) |
| 仓库变更记录 | [CHANGELOG.md](CHANGELOG.md) |

## 仓库目录

```text
brand/
├── README.md
├── README.zh-CN.md
├── PLAN.md
├── CHANGELOG.md
├── guidelines/
│   ├── brand-guidelines.md
│   ├── logo-usage.md
│   ├── seal-usage.md
│   ├── typography.md
│   └── licensing.md
├── design-tokens/
│   ├── colors.json
│   └── typography.json
├── sources/
│   ├── logo/
│   └── seal/
├── exports/
│   ├── svg/
│   ├── png/
│   ├── og/
│   └── favicon/
└── references/
```

Git 无法跟踪空目录。**目前仅印章 V1.1 的 PNG 和宣纸预览已上传**；其他图像、SVG 和字体仍未入库。

## 后续素材命名

建议采用 `pw-<内容>-<变体>-<尺寸可选>-v<主版本.次版本>.<扩展名>`。

以下除特别注明为示例的文件外，Mark 与印章 PNG 均已上传：

- [极简 Mark V1.0 透明 PNG](exports/png/pw-mark-minimal-transparent-v1.0-2048.png)（已上传）；`pw-mark-minimal-light-v1.1.svg`（仅示例，SVG 暂缓）
- [标准 Mark V1.1 透明 PNG](exports/png/pw-mark-standard-seal-v1.1-2048.png)（已上传）；`pw-mark-standard-seal-v1.1.svg`（仅示例）
- `pw-github-avatar-1024-v1.1.png`
- `pw-readme-banner-v1.1.png`
- `pw-og-general-1200x630-v1.1.png`
- `pw-github-social-1280x640-v1.1.png`
- 印章 V1.1：[4096px 正式透明 PNG](exports/png/pw-seal-zhi-cinnabar-enlarged-v1.1-4096.png) · [2048px](exports/png/pw-seal-zhi-cinnabar-enlarged-v1.1-2048.png) · [1024px](exports/png/pw-seal-zhi-cinnabar-enlarged-v1.1-1024.png)；[宣纸效果图](references/pw-seal-zhi-on-paper-proof-v1.1.png)。SVG 暂缓。

尚未批准的稿件请放在 `references/`，或在文件名中标注 `draft`，不得与正式导出物混放。

**品牌文件与代码授权是两回事。** 不因组织开源仓库使用某种代码许可证，就推定 Logo、印章、插画、字体同时获得相同许可。详细见[授权说明](guidelines/licensing.md)。

参与组织开源项目请参考[共享贡献与社区规范](https://github.com/primordialweave/.github)。
