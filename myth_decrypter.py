
# 🔐 MythOS Decrypter v1.0
# Author: Han aka gone2soon

import os
import json
import base64
from pathlib import Path

DECRYPTABLE_EXTENSIONS = ['.rpl', '.glyph', '.clr', '.myth', '.txt']

def decrypt_mythic_file(filepath):
    if not any(filepath.endswith(ext) for ext in DECRYPTABLE_EXTENSIONS):
        print(f"[x] Unsupported file type: {filepath}")
        return

    try:
        with open(filepath, 'rb') as f:
            encoded_data = f.read()
            decoded = base64.b64decode(encoded_data).decode('utf-8')
            print(f"\n🔓 Decrypted → {filepath}\n")
            print(decoded)
    except Exception as e:
        print(f"[!] Error decrypting {filepath}: {e}")

def myth_decrypt_dir(directory):
    print(f"💾 Scanning directory: {directory}")
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        if os.path.isfile(full_path):
            decrypt_mythic_file(full_path)

if __name__ == "__main__":
    print("🧠 MythOS Decrypter Initialized\n")
    target_dir = input("📁 Enter path to folder with encrypted files: ").strip()

    if not Path(target_dir).exists():
        print(f"[x] Folder not found: {target_dir}")
    else:
        myth_decrypt_dir(target_dir)
