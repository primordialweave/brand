# Primordial Weave · Logo / Mark 使用规范

> **当前正式图形：极简 Mark V1.0；标准 Mark V1.2 居中版（配印章 V1.4）。** 2026-11-09 品牌方视觉确认，旧 V1.1 均保留。完整图形不再使用生成模型重画。

## 当前入口

| 项目 | 文件 |
| --- | --- |
| 标准 Mark（首选） | [透明 2048](../exports/png/pw-mark-standard-seal-v1.2-centered-2048.png) |
| 极简 Mark（无印章） | [透明 2048](../exports/png/pw-mark-minimal-transparent-v1.0-2048.png) |
| 崇羲参考「織」印章 V1.4 | [透明 4096](../exports/png/pw-seal-zhi-chongxi-v1.4-4096.png) |
| 英文 / 中文 / 中英字标 | [EN](../exports/png/pw-wordmark-horizontal-en-v1.1-2400x600.png) · [ZH](../exports/png/pw-wordmark-horizontal-zh-v1.0-2400x600.png) · [双语](../exports/png/pw-wordmark-horizontal-bilingual-v1.0-2400x600.png) |
| 组织头像 | [1024 PNG](../exports/png/pw-github-avatar-v1.0-1024.png) |

## 锁定排版

- 2048×2048 RGBA 真透明画布。
- 极简 Mark 母图缩放为 1760×1760，位置 (143,152)。
- 印章透明容器为 304×304，位置 (1482,1482)，从 V1.4 正式 2048 PNG 等比适配。
- 此处是**居中对齐修订方案**，不是早期 V1.2 严格齐边草案；其说明见 [V1.2 居中规范](MARK-COMPOSITION-SPEC-V1.2-CENTERED.md)。
- 太极墨环、金环、双朱砂点以及原始纹理必须与极简 Mark V1.0 一致。

## 禁止操作

- 不重新用 AI 生成图形或猜测「織」字笔画；不要把视觉近似图替换正式二进制文件。
- 不拉伸变形、改色、重绘金环、修改印章字形、添加背景光晕或将太极浅色区抠成透明。
- 小尺寸 Favicon 应使用独立适配版，不将带印章的复杂 Mark 强缩至 16px。
- 深色应用场景需要检查实际对比度；现有浅底标准 Mark 不应宣称已优化所有深底。

## 复现与版本

- [精确合成脚本](../sources/logo/scripts/compose_seal_and_mark_v1_4.py) · [QA](../sources/seal/qa-v1.4.json) · [Mark manifest](../sources/logo/manifest.json)。
- V1.1 旧版 [Mark](../exports/png/pw-mark-standard-seal-v1.1-2048.png) 仍保留，旧 [V1.1 规范](MARK-COMPOSITION-SPEC.md) 只用于历史复现。
- README Banner、OG、Social Preview 当前仍使用旧印章，需要另行升级，仓库归档不等于组织 `.github` 主页已替换。
- 品牌字形为基于参考图描摹的篆刻艺术，不等同历史正字学认证或第三方开放授权。
