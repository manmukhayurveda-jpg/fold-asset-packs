# Sources

| Pack | Source | Selection | Rights |
|---|---|---|---|
| `ma_visuals` v1 | Manmukh Ayurveda Shopify, metaobject `ma_svg_asset` ("MA Visual Asset Library", 180 entries; 150 with a file) | 135 entries in subject categories (conditions, laboratory, herbs, care); trust, commerce and contact icons excluded | © Manmukh Ayurveda. Distributed only for use inside the Fold AI Video Studio app. Not medically reviewed. |
| `hindi_voice` v1 | Kokoro-82M v1.0 by hexgrad (https://huggingface.co/hexgrad/Kokoro-82M), int8 ONNX from k2-fsa/sherpa-onnx release `kokoro-int8-multi-lang-v1_0` | The model, its token list and the four Hindi voice styles (speaker ids 31-34) | Apache-2.0; LICENSE and NOTICE.md travel inside the archive. Built with `scripts/assets/build_hindi_voice_pack.py` in the app repository. |
| `clinical_3d` v1 | BodyParts3D 4.0, © The Database Center for Life Science, CC BY 4.0 (https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html) | Six models from FMA concepts: airways, leg bones and knee, lumbar spine, pelvis, digestive organs, body surface. Built with `scripts/assets/build_clinical3d_pack.py` | CC BY 4.0 with attribution in the manifest and NOTICE.md. **Not yet medically reviewed**; review by the Manmukh Ayurveda doctors is recorded in a later version. |

Depth maps were estimated offline with Depth Anything V2 **Small** (Apache-2.0). Larger Depth Anything V2 variants
carry non-commercial terms and are not used.
