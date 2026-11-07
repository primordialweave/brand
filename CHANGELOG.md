# Changelog · Primordial Weave Brand

This log records **repository documentation and approved asset releases separately**. An entry about documentation does not certify a brand master or historical glyph.

## Unreleased

- Other brand assets, including the Logo / Mark / Banner / OG / avatar, are not replaced by the current seal release. SVG and final art licensing remain pending.

## 2026-11-07 · Standard Mark V1.1 approved and documented

- Verified `exports/png/pw-mark-standard-seal-v1.1-2048.png`, `guidelines/MARK-COMPOSITION-SPEC.md`, and `sources/logo/scripts/compose_mark.py` match the previously delivered three-file ZIP by Git blob SHA-1 and size.
- Brand owner approved the V1.1 composition: 2048px RGBA canvas, minimal Mark 1760px at (55,50), approved seal 304px at (1480,1460).
- Corrected the Python script to read its locked source PNGs from the repository's actual `exports/png/` directory, with non-destructive output at `build/standard-mark-v1.1/`.
- Local repository-layout smoke test reproduced the already published PNG byte for byte; SHA-256: `1b776f96c9dcbcfe6838bd07c0d737916496e13b3e27114e4cea2da9110c1175`.
- Added `sources/logo/ASSET-RECORD.md` and `sources/logo/manifest.json`, synchronized English/Chinese README and logo guideline status.
- No PNG binaries were modified or re-uploaded in these documentation commits; the organization `.github` Banner/OG/avatar remain unchanged. SVG and dark-mode-specialized artwork are pending.

## 2026-11-07 · Seal PNG V1.1 published and indexed

- Set branded `織` seal **V1.1** as the current approved visual version and mark V1.0 as historical.
- Confirmed 4096, 2048 and 1024px transparent PNG exports under `exports/png/`, and the rice-paper display image under `references/`, already exist in the repo.
- Independently compared Git blob SHA-1 values and file sizes with the original V1.1 package; all four files matched. SHA-256 values recorded in [asset record](sources/seal/ASSET-RECORD.md).
- Updated `sources/seal/manifest.json`, added historical `manifest-v1.0.json`, and synchronized bilingual READMEs and seal usage documentation.
- Original 1254px raster source and final editable SVG are **not** in the repository. Upscaled 4096px PNG is not native 4K source detail.
- **No binary images were replaced or uploaded in this documentation commit.** No change to Mark, Banner, OG, or avatar and no general-use brand license issued.


## 2026-11-06 · Seal visual approval V1.0

- Approved the branded cinnabar `織` seal as the official visual artwork (not as academically certified standard small-seal script).
- Locked source file `pw-seal-zhi-cinnabar-v1.0.png` (1254×1254 RGBA), SHA-256: `a323d4c77a01e8f1a0b1e0859cee967bb49ac9bb3b56921c0c1b61e6381f4670`.
- Added [asset record](sources/seal/ASSET-RECORD.md) and [manifest](sources/seal/manifest.json) without uploading or changing any existing artwork.
- No images replaced; no SVG created; no public brand-art license granted.

## 2026-11-06 · docs-first baseline

### Added
- English and Chinese brand README entrypoints.
- Brand, logo, seal, typography and licensing text guidelines.
- Candidate machine-readable color and typography tokens reflecting the latest S1 PNG working guideline.
- Placeholder documentation for `sources/`, `exports/` and `references/` directories.
- Copied organization execution PLAN with section 10 implementation notes.

### Notes
- Branding and visual-rights approval remain outstanding.
- The `織` glyph requires explicit source-based expert review before it is described as authentic standard small-seal script.
- No logos, images, SVGs or font binaries are included.
