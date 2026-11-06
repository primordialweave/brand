# Primordial Weave · Brand System

<p align="center">
  <strong>Inspired by ancient wisdom. Built for the open future.</strong>
</p>

<p align="center">
  <a href="./README.md">English</a> · <a href="./README.zh-CN.md">简体中文</a>
</p>

The **Primordial Weave (原初织界)** brand draws on Chinese philosophy, ink-wash aesthetics, and thoughtful modern open-source design.

> **Status · Seal V1.1 current (2026-11-07).** The approved **織 cinnabar brand seal V1.1** is now uploaded as three transparent PNG sizes plus a paper preview. The [current manifest](sources/seal/manifest.json) and [asset record](sources/seal/ASSET-RECORD.md) give exact files and hashes. V1.0 remains documented as superseded history. Logo/Mark, Banner, OG and avatar files have **not** been replaced; SVG remains deferred. This is brand artwork, not a scholarly certification of seal-script glyphs or a public-use license.

## Documentation

| Area | Document |
| --- | --- |
| Brand direction and constraints | [Brand guidelines](guidelines/brand-guidelines.md) |
| Taiji, circle and logo usage | [Logo usage](guidelines/logo-usage.md) |
| Cinnabar seal V1.1 usage and verification limits | [Seal usage](guidelines/seal-usage.md) · [asset record](sources/seal/ASSET-RECORD.md) |
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
│   ├── png/            # Approved V1.1 transparent seal PNGs
│   ├── og/             # Reserved
│   └── favicon/        # Reserved
└── references/         # V1.1 paper proof + future labeled references
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
- [V1.1 4096px master PNG](exports/png/pw-seal-zhi-cinnabar-enlarged-v1.1-4096.png), [2048px](exports/png/pw-seal-zhi-cinnabar-enlarged-v1.1-2048.png), [1024px](exports/png/pw-seal-zhi-cinnabar-enlarged-v1.1-1024.png) and [paper proof](references/pw-seal-zhi-on-paper-proof-v1.1.png). SVG remains deferred.

Unapproved explorations must include `draft` in their filename or live in `references/`. Never mix them with approved exports.

## Rights and participation

This is a **public reference repository**, not a blanket permission to reuse the brand. No brand-asset license is granted by its public visibility. Code, docs, typography and visual assets have separate rights and approvals; read [Licensing](guidelines/licensing.md) before reuse. Do not commit font files or unverified third-party material.

For open-source contribution and community policy, see [Primordial Weave's organization defaults](https://github.com/primordialweave/.github). Changes to core identity should be reviewed and recorded before publication.
