# Logo Source & Reproducible Standard Mark

2026-11-07：极简 Mark V1.0 三版 PNG、原始位图、标准 Mark V1.1 透明 PNG、合成规范和可执行脚本均已上传。标准 Mark V1.1 为品牌方批准的图形版本。

## 文件入口

- [原始极简 Mark 1254px PNG](mark-minimal-source-1254.png)：源位图（不是 SVG）。
- [极简 Mark V1.0 透明版](../../exports/png/pw-mark-minimal-transparent-v1.0-2048.png)：合成主体。
- [「織」朱砂印章 V1.1](../../exports/png/pw-seal-zhi-cinnabar-enlarged-v1.1-4096.png)：合成印章。
- [标准 Mark V1.1 透明版](../../exports/png/pw-mark-standard-seal-v1.1-2048.png)：已批准输出。
- [合成脚本](scripts/compose_mark.py)、[精确合成规范](../../guidelines/MARK-COMPOSITION-SPEC.md)。
- [资产登记](ASSET-RECORD.md)、[机器可读 Manifest](manifest.json)。

## 可重复构建

```bash
python3 -m pip install Pillow
python3 sources/logo/scripts/compose_mark.py
```

在仓库根目录执行。脚本会验证两份已锁定输入文件的 SHA-256，默认在 `build/standard-mark-v1.1/` 创建新的 PNG 和检查预览，不覆盖已发布文件。经本地仓库布局验证，生成 PNG 的 SHA-256 与 GitHub 定稿文件相同。

SVG、深色专用版、横向字标、Banner、OG、头像和 favicon 仍需独立完成。印章属于品牌化篆刻设计，不宣称规范小篆学术认证。
