# Primordial Weave · Brand System

<p align="center"><strong>Inspired by ancient wisdom. Built for the open future.</strong></p>

<p align="center"><a href="./README.md">English</a> · <a href="./README.zh-CN.md">简体中文</a></p>

Primordial Weave (原初织界) brings together Chinese philosophical imagery, ink-wash aesthetics and open-source product design.

> **Official identity update · 2026-11-09:** Minimal Mark V1.0; **Standard Mark V1.2 centered** using the **Chongxi-reference 織 seal V1.4**. Both approved images and their recorded hashes are published. V1.1 stays in the history. GitHub organization `.github` banners/OG/avatar are not automatically replaced.

## Current approved artwork

| Asset | File |
| --- | --- |
| Standard Mark V1.2 centered | [2048px PNG](exports/png/pw-mark-standard-seal-v1.2-centered-2048.png) |
| Seal V1.4 | [4096px](exports/png/pw-seal-zhi-chongxi-v1.4-4096.png) · [2048px](exports/png/pw-seal-zhi-chongxi-v1.4-2048.png) · [1254px](exports/png/pw-seal-zhi-chongxi-v1.4-1254.png) |
| Minimal Mark V1.0 | [2048px PNG](exports/png/pw-mark-minimal-transparent-v1.0-2048.png) |
| English/Chinese wordmarks | [EN](exports/png/pw-wordmark-horizontal-en-v1.1-2400x600.png) · [ZH](exports/png/pw-wordmark-horizontal-zh-v1.0-2400x600.png) · [bilingual](exports/png/pw-wordmark-horizontal-bilingual-v1.0-2400x600.png) |
| GitHub avatar | [PNG](exports/png/pw-github-avatar-v1.0-1024.png) |
| README Banner / OG / Social Preview | [Banner](exports/png/pw-readme-banner-v1.1-seal-top-right-2400x600.png) · [OG](exports/og/pw-og-share-v1.0-1200x630.png) · [Preview](exports/og/pw-github-social-preview-v1.0-1280x640.png) (older seal artwork; not yet refreshed) |
| Favicon | [Sizes & ICO](exports/favicon/README.md) |

## Documentation

| Topic | Guide |
| --- | --- |
| Identity & philosophy | [Brand guidelines](guidelines/brand-guidelines.md) |
| Mark | [Logo usage](guidelines/logo-usage.md) · [approved centered layout](guidelines/MARK-COMPOSITION-SPEC-V1.2-CENTERED.md) · [manifest](sources/logo/manifest.json) |
| Seal | [Seal usage](guidelines/seal-usage.md) · [manifest](sources/seal/manifest.json) · [QA](sources/seal/qa-v1.4.json) |
| Typography & rights | [Typography](guidelines/typography.md) · [Licensing](guidelines/licensing.md) |
| Project roadmap | [PLAN.md](PLAN.md) · [CHANGELOG.md](CHANGELOG.md) |

## Rebuild approved PNG assets

```bash
python3 -m pip install -r sources/logo/scripts/requirements-v1.4.txt
python3 sources/logo/scripts/compose_seal_and_mark_v1_4.py
python3 sources/logo/scripts/verify_assets_v1_4.py
```

Rebuild outputs are written under `build/v1.4/`, not over the approved exports. SHA-256, traced glyph source and exact layer coordinates are in the manifests.

**Use and licensing:** The seal glyph was traced from a small reference image, not typeset from an installed Chongxi font. Visual approval is not a statement of academic seal-script authenticity, third-party rights clearance or a public brand-art license. See [Licensing](guidelines/licensing.md).
