# Logo sources and approved Mark

**Current Mark:** V1.2 centered with V1.4 approved 「織」 seal (2026-11-09). Minimal Mark V1.0 is unchanged.

- [Approved Mark PNG](../../exports/png/pw-mark-standard-seal-v1.2-centered-2048.png) · [minimal Mark master](../../exports/png/pw-mark-minimal-transparent-v1.0-2048.png)
- [Approved seal V1.4](../../exports/png/pw-seal-zhi-chongxi-v1.4-4096.png)
- [Approved glyph SVG trace](zhi-chongxi-approved-outline-v1.1.svg) · [clean baseplate](seal-baseplate-v1.0-1254.png)
- [Centered layout specification](../../guidelines/MARK-COMPOSITION-SPEC-V1.2-CENTERED.md) · [Mark manifest](manifest.json) · [Mark asset record](ASSET-RECORD.md)
- [Composer](scripts/compose_seal_and_mark_v1_4.py) · [Verifier](scripts/verify_assets_v1_4.py)

From the repository root:

```bash
python3 -m pip install -r sources/logo/scripts/requirements-v1.4.txt
python3 sources/logo/scripts/compose_seal_and_mark_v1_4.py
python3 sources/logo/scripts/verify_assets_v1_4.py
```

Newly generated PNGs are placed in `build/v1.4/` rather than overwriting approved exports. The formerly approved V1.1 Mark and its [historical script](scripts/compose_mark.py) remain reproducible.

Note: V1.2 **centered** is a different approved layout from the earlier unapproved strict-corner draft. SVG is currently only the glyph trace, not the complete Mark.
