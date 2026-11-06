# Primordial Weave · 原初织界品牌规范

<p align="center">
  <strong>灵感源自古老智慧，创造面向开放未来的工具。</strong>
</p>

<p align="center">
  <a href="./README.md">English</a> · <a href="./README.zh-CN.md">简体中文</a>
</p>

**Primordial Weave（原初织界）** 是以中国传统哲学、水墨审美和现代开源精神为灵感的品牌。

> **当前状态：正式采用「織」朱砂品牌印章 V1.0，其余视觉继续打磨（2026-11-06）。** 印章 PNG 原图已在本地交付包中锁定，GitHub 仓库已登记版本及校验值，但**尚未上传该二进制 PNG**。Mark、Banner、OG、头像及 SVG 都保持原状。此印章属于品牌化篆刻设计，不宣称其为已通过古文字学认证的标准小篆字形。公开仓库不等于开放商业授权。

## 文档导航

| 内容 | 文件 |
| --- | --- |
| 品牌定位、理念、视觉原则 | [品牌规范](guidelines/brand-guidelines.md) |
| 标志和太极使用 | [Logo 使用规范](guidelines/logo-usage.md) |
| 正式印章 V1.0 与文化考证边界 | [印章使用规范](guidelines/seal-usage.md) · [资产记录](sources/seal/ASSET-RECORD.md) |
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

Git 无法跟踪空文件夹，因此留空的素材目录只放 `README.md` 说明文件，**不放任何图片、SVG 或字体**。

## 后续素材命名

建议采用 `pw-<内容>-<变体>-<尺寸可选>-v<主版本.次版本>.<扩展名>`。

下面均是**命名示例，不代表对应文件已存在**：

- `pw-mark-minimal-light-v1.1.svg`
- `pw-mark-standard-seal-v1.1.svg`
- `pw-github-avatar-1024-v1.1.png`
- `pw-readme-banner-v1.1.png`
- `pw-og-general-1200x630-v1.1.png`
- `pw-github-social-1280x640-v1.1.png`
- `pw-seal-zhi-cinnabar-v1.0.png`（**本地已定稿，尚待上传 GitHub**；SVG 暂缓）

尚未批准的稿件请放在 `references/`，或在文件名中标注 `draft`，不得与正式导出物混放。

**品牌文件与代码授权是两回事。** 不因组织开源仓库使用某种代码许可证，就推定 Logo、印章、插画、字体同时获得相同许可。详细见[授权说明](guidelines/licensing.md)。

参与组织开源项目请参考[共享贡献与社区规范](https://github.com/primordialweave/.github)。
