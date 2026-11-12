# Fold AI Video Studio asset packs

Release files the Fold AI Video Studio app downloads from *Settings > Visual asset pack*.

- `ma_visuals_v1.zip`: 135 medical and Ayurveda illustrations from the Manmukh Ayurveda "MA Visual Asset Library",
  each named by its library key (`ma_<canonical_key>.webp`), with a depth map (`depth/*.png`) and `manifest.json`
  (English and Hindi search words, source handle, SHA-256). Illustrations, not medically reviewed anatomy.

The app checks every download against the SHA-256 built into it and refuses any other file.
Artwork © Manmukh Ayurveda; not licensed for reuse outside the app.
