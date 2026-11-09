# Primordial Weave · Scenic Media V1.1/V1.2 · QA

**核验时间：2026-11-10。** 此记录证明仓库文件与交付素材一致，不等于已更新组织主页或完成 GitHub 分享图设置。

## 文件完整性（4/4 一致）

| 当前文件 | 尺寸 | 字节数 | SHA-256 | Git blob SHA-1 |
| --- | --- | ---: | --- | --- |
| [README Banner](../../exports/png/pw-readme-banner-scenic-composed-v1.1-2400x600.png) | 2400×600 | 1897453 | `eb405f6264159f655402fb826346fcde10a0a0453e2b4d2f9c6c5d927d4bbe4e` | `13d83d180ab10cacd86ece106839340ede4ecf2c` |
| [OG](../../exports/png/pw-og-share-scenic-composed-v1.2-1200x630.png) | 1200×630 | 1183544 | `430c333a3d2666d5a53473dcf8d37ac4bb2475de919943979df962f708847da0` | `318adc15899f2f39cdb003f0989942fdec67acf4` |
| [Social Preview](../../exports/png/pw-github-social-preview-scenic-composed-v1.2-1280x640.png) | 1280×640 | 1194152 | `9ef11f2433dc0c14765ca5088259ccef4bb12d0c59b6c7d04ebf4471ac8dc98b` | `81c3479dbf25c66973fc0690992a62cbe661c790` |
| [Social Preview optimized PNG](../../exports/png/pw-github-social-preview-scenic-composed-v1.2-1280x640-github-optimized.png) | 1280×640 | 571295 | `b3c47e4120ce60cf869046d1345a98dbf137f8a9bd24bfbc9c1b664a66e25cd5` | `4991a3d3972a5b3fb14df2ac3710b647dd9ee8c5` |

- README Banner 采用 V1.1，OG 与 Social Preview 采用 V1.2，GitHub 优化 PNG 为 571,295 字节（小于 1,000,000 字节）。
- 三张干净 AI 背景分别位于 `sources/backgrounds/`，定稿极简 Mark V1.0、印章 V1.4、英文字标 V1.1 和标语以 Pillow 程序精确叠加；AI 没有重画品牌图层。
- 原合成脚本上传后路径仍指向交付包中的 `sources/brand`。现已改为仓库的 `exports/png`、`sources/backgrounds`，仅输出到 `build/scenic-v1.2/`，不会覆盖正式图片。
- **验收边界：** 本次独立核对了四张 PNG 的字节和哈希；修正后的仓库合成脚本未在本次执行中完成端到端重复构建，应在后续干净环境运行并比较 SHA-256。
- **仍未同步：** `primordialweave/.github/profile/README.md` 及中文版引用的 `.github/assets/primordial-weave-banner.png` 是独立旧图，`brand` 新素材不会自动替换它，也不会自动配置 GitHub Settings 中的 Social Preview。

[Manifest](scenic-exports-manifest-v1.2.json) · [Python script](scripts/compose.py)
