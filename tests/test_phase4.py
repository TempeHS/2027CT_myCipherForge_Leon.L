from engine import phase4_encrypt, phase4_decrypt

key = {
    "shift": 5,
    "block_size": 4,
    "password": "SECRET",
    "noise_interval": 3,
    "noise_char": "~",
}

test = "HELLO WORLD"
noisy = phase4_encrypt(test, key)
print(f"Original:  {test}")
print(f"With noise: {noisy}")
print(f"Cleaned:   {phase4_decrypt(noisy, key)}")
