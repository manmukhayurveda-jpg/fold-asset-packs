#!/usr/bin/env python3
"""Checks a pack archive the way the app does before publishing it (no Android code, no network).

    python3 tools/verify_pack.py ma_visuals_v1.zip [--sha256 <expected>] [--catalog catalog/v1/catalog.json]

Fails on: unsafe paths, code or unknown file types, duplicate names, too many files or bytes, missing manifest,
missing or mismatched files, images that do not decode (needs Pillow), and a catalog entry whose size or hash differs.
"""
import argparse, hashlib, io, json, sys, zipfile

ALLOWED = {"webp", "png", "jpg", "jpeg", "json", "gltf", "glb", "txt", "md"}
MAX_ENTRIES, MAX_ENTRY, MAX_TOTAL = 4000, 40 << 20, 600 << 20


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("zip"); ap.add_argument("--sha256"); ap.add_argument("--catalog")
    a = ap.parse_args()
    raw = open(a.zip, "rb").read(); digest = hashlib.sha256(raw).hexdigest(); problems = []
    if a.sha256 and digest != a.sha256: problems.append(f"archive sha256 {digest} != {a.sha256}")
    if a.catalog:
        entry = next((p for p in json.load(open(a.catalog))["packs"] if p["sha256"] == digest), None)
        if not entry: problems.append("archive is not listed in the catalog")
        elif entry["bytes"] != len(raw): problems.append("catalog size differs")
    z = zipfile.ZipFile(io.BytesIO(raw)); infos = z.infolist(); names = [i.filename for i in infos]
    if len(infos) > MAX_ENTRIES: problems.append("too many files")
    if len({n.lower() for n in names}) != len(names): problems.append("duplicate names")
    if sum(i.file_size for i in infos) > MAX_TOTAL: problems.append("unpacks too large")
    for i in infos:
        n = i.filename
        if n.startswith("/") or ".." in n.split("/"): problems.append(f"unsafe path {n}")
        if not n.endswith("/") and n.rsplit(".", 1)[-1].lower() not in ALLOWED: problems.append(f"file type not allowed: {n}")
        if i.file_size > MAX_ENTRY: problems.append(f"{n} too large")
    try:
        m = json.loads(z.read("manifest.json"))
    except KeyError:
        print("FAIL: no manifest.json"); sys.exit(1)
    try:
        from PIL import Image
    except ImportError:
        Image = None
    ids = set()
    for asset in m.get("assets", []):
        if asset["id"] in ids: problems.append(f"duplicate id {asset['id']}")
        ids.add(asset["id"])
        for key in ("file", "depth"):
            rel = asset.get(key)
            if not rel: continue
            if rel not in names: problems.append(f"{asset['id']}: {rel} missing"); continue
            data = z.read(rel)
            if Image is not None and rel.rsplit(".", 1)[-1].lower() in {"webp", "png", "jpg", "jpeg"}:
                try: Image.open(io.BytesIO(data)).verify()
                except Exception: problems.append(f"{rel} does not decode")
        if asset.get("sha256") and asset.get("file") in names and hashlib.sha256(z.read(asset["file"])).hexdigest() != asset["sha256"]:
            problems.append(f"{asset['id']}: hash mismatch")
    print(f"{len(m.get('assets', []))} assets, {len(infos)} files, {sum(i.file_size for i in infos)} bytes unpacked, sha256 {digest}")
    for p in problems: print("FAIL:", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
