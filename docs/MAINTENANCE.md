# Publishing a pack version

1. Build the archive in the private app repository (`scripts/assets/build_ma_pack.py`).
2. `python3 tools/verify_pack.py <zip>` must pass.
3. Create a **new** release tag (`<pack>-v<N>`); never replace bytes under an existing tag.
4. Add the entry to `catalog/v1/catalog.json` (url, bytes, sha256, fileCount, capabilities, minRenderContract).
5. Sign it on the owner's Mac (the private key never goes to GitHub):
   `openssl dgst -sha256 -sign ~/.fold_video/packs/catalog_signing_key.pem catalog/v1/catalog.json | base64 > catalog/v1/catalog.json.sig`
6. Commit both files. The app accepts the catalog only if the signature matches its built-in public key.

To withdraw a version set `"revoked": true` and re-sign. Installed copies stop being offered by the app.
