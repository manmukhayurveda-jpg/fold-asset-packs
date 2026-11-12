# Fold AI Video Studio asset packs

Release files the Fold AI Video Studio app downloads from *Settings > Visual asset pack*.

- `ma_visuals_v1.zip`: 135 medical and Ayurveda illustrations from the Manmukh Ayurveda "MA Visual Asset Library",
  each named by its library key (`ma_<canonical_key>.webp`), with a depth map (`depth/*.png`) and `manifest.json`
  (English and Hindi search words, source handle, SHA-256). Illustrations, not medically reviewed anatomy.

The app checks every download against the SHA-256 built into it and refuses any other file.
Artwork © Manmukh Ayurveda; not licensed for reuse outside the app.

## Layout

- `catalog/v1/catalog.json` + `.sig`: the signed list of pack versions the app may install.
- `schemas/`: catalog and manifest formats. `manifests/`: the manifest of each released pack.
- `tools/verify_pack.py`: the checks a pack must pass before it is released. `provenance/`, `docs/MAINTENANCE.md`.
- Pack archives are GitHub Release files, never committed to git.
