# Primordial Weave · Brand System

<p align="center">
  <strong>Inspired by ancient wisdom. Built for the open future.</strong>
</p>

<p align="center">
  <a href="./README.md">English</a> · <a href="./README.zh-CN.md">简体中文</a>
</p>

The **Primordial Weave (原初织界)** brand draws on Chinese philosophy, ink-wash aesthetics, and thoughtful modern open-source design.

> **Status · Seal V1.0 visually approved / other graphics under refinement** (2026-11-06). The **織 cinnabar seal has been approved as brand artwork V1.0** and recorded in [its asset record](sources/seal/ASSET-RECORD.md), but **its PNG has not yet been uploaded to GitHub**. Other images, SVGs and fonts are unchanged and remain under refinement. Small-seal glyph scholarly certification is not claimed.

## Documentation

| Area | Document |
| --- | --- |
| Brand direction and constraints | [Brand guidelines](guidelines/brand-guidelines.md) |
| Taiji, circle and logo usage | [Logo usage](guidelines/logo-usage.md) |
| Cinnabar seal V1.0 usage and verification limits | [Seal usage](guidelines/seal-usage.md) · [asset record](sources/seal/ASSET-RECORD.md) |
| Chinese/English typography | [Typography](guidelines/typography.md) |
| Licensing and attribution | [Licensing policy](guidelines/licensing.md) |
| Candidate color tokens | [colors.json](design-tokens/colors.json) |
| Candidate typography tokens | [typography.json](design-tokens/typography.json) |
| Ecosystem roadmap | [PLAN.md](PLAN.md) |
| Update history | [CHANGELOG.md](CHANGELOG.md) |

## Structure

```text
brand/
├── README.md / README.zh-CN.md
├── PLAN.md / CHANGELOG.md
├── guidelines/
├── design-tokens/
├── sources/
│   ├── logo/           # Reserved; no artwork committed
│   └── seal/           # Reserved; no artwork committed
├── exports/
│   ├── svg/            # Reserved
│   ├── png/            # Reserved
│   ├── og/             # Reserved
│   └── favicon/        # Reserved
└── references/         # Reserved; drafts will be labeled clearly
```

Git does not store empty directories, so reserved folders contain `README.md` documentation rather than asset files.

## Naming

Use `pw-<subject>-<variant>-<dimensions-if-needed>-v<major.minor>.<ext>` for **future** asset releases. Examples only (not yet present):

- `pw-mark-minimal-light-v1.1.svg`
- `pw-mark-standard-seal-v1.1.svg`
- `pw-github-avatar-1024-v1.1.png`
- `pw-readme-banner-v1.1.png`
- `pw-og-general-1200x630-v1.1.png`
- `pw-github-social-1280x640-v1.1.png`
- `pw-seal-zhi-cinnabar-v1.0.png` — **approved offline PNG**, not yet present in this GitHub repository; vector SVG deferred

Unapproved explorations must include `draft` in their filename or live in `references/`. Never mix them with approved exports.

## Rights and participation

This is a **public reference repository**, not a blanket permission to reuse the brand. No brand-asset license is granted by its public visibility. Code, docs, typography and visual assets have separate rights and approvals; read [Licensing](guidelines/licensing.md) before reuse. Do not commit font files or unverified third-party material.

For open-source contribution and community policy, see [Primordial Weave's organization defaults](https://github.com/primordialweave/.github). Changes to core identity should be reviewed and recorded before publication.
