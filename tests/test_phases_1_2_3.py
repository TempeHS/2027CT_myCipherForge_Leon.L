"""Test the full Phase 1 + Phase 2 + Phase 3 pipeline.

Run from the project root with:  python tests/test_phases_1_2_3.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import encrypt, decrypt
from engine import phase1_encrypt, phase2_encrypt, phase3_encrypt

# Key with all settings
key = {
    "shift": 7,  # Phase 1
    "block_size": 4,  # Phase 2
    "password": "FORGE",  # Phase 3
}

message = "CipherForge 2026!"

# Watch each phase transform the message
print(f"Original:       {message}")

after_p1 = phase1_encrypt(message, key)
print(f"After Phase 1:  {after_p1}")

after_p2 = phase2_encrypt(after_p1, key)
print(f"After Phase 2:  {after_p2}")

after_p3 = phase3_encrypt(after_p2, key)
print(f"After Phase 3:  {after_p3}")

# Full encrypt/decrypt
encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print(f"\nFull encrypt: {encrypted}")
print(f"Decrypted:    {decrypted}")
print(f"Success: {decrypted == message}")

###############################################
# PHASE 4: NOISE INJECTION
###############################################


def phase4_encrypt(text, key):
    """Insert noise character every N positions."""
    interval = key.get("noise_interval", 3)
    noise = key.get("noise_char", "~")

    result = ""
    count = 0

    for char in text:
        result += char
        count += 1
        # Insert noise after every N real characters
        if count % interval == 0:
            result += noise

    return result


def phase4_decrypt(text, key):
    """Remove noise characters at their known positions."""
    interval = key.get("noise_interval", 3)

    result = ""
    real_count = 0
    i = 0

    while i < len(text):
        result += text[i]
        real_count += 1
        i += 1

        # Skip the noise character after every N real characters
        if real_count % interval == 0 and i < len(text):
            i += 1  # Skip noise

    return result
