import os
import hashlib

BASE_PATH = "packfiles/bettermc"
OUTPUT_FILE = "packs/bettermc/manifest.json"

GITHUB_BASE = "https://raw.githubusercontent.com/serverwhisp/tits-launcher/main/packfiles/bettermc"


def sha1_file(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


files = []

for root, _, filenames in os.walk(BASE_PATH):
    for name in filenames:
        full_path = os.path.join(root, name)

        rel_path = os.path.relpath(full_path, BASE_PATH).replace("\\", "/")

        url = f"{GITHUB_BASE}/{rel_path}"

        print(f"Обрабатываю: {rel_path}")

        files.append({
            "path": rel_path,
            "url": url,
            "sha1": sha1_file(full_path)
        })


os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

import json
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump({"files": files}, f, indent=2, ensure_ascii=False)

print("\nГотово: manifest.json создан")