# 🔐 CipherForge

**A 5-phase encryption algorithm built from scratch in Python.

## Description 

CipherForge is an educational encryption system that demonstrates how real-world encryption algorithms like AES work. It applies 5 layers of transformation to convert plaintext into unreadable ciphertext.

## About

This project implements a multi-layered encryption system that I designed from scratch. Each layer adds a different type of protection, similar to how real encryption algorithms like AES work.

## Fetures

- **5-phase encryption pipeline**
- **Web interface** for easy encryption/decryption
- **Key-based security** with trillions of combinations
- **Automated test suite** for verification

## The Phase 5

| Phase | Name | Description |
|-------|------|-------------|
| 1 | Substitution | Shifts all characters by a fixed amount |
| 2 | Transposition | Reverses characters in blocks |
| 3 | Key-Dependent | Uses password for variable shifting |
| 4 | Noise Injection | Adds decoy characters |
| 5 | Wild Card | [YOUR DESCRIPTION HERE] |

## Getting Started

### Run In Codespaces

1. Click **Code** → **Codespaces** → **Create codespace**
2. Wait for environment to load
3. Run: `python app.py`
4. Open the Ports tab and click the globe icon for port 5000

### Run Tests

```bash
python test_engine.py
```

## Key Format 

The encryption key is a dictionary with these fields:

```python
key = {
    "shift": 5,              # Phase 1: shift amount (1-94)
    "block_size": 4,         # Phase 2: block size (2-20)
    "password": "SECRET",    # Phase 3: encryption password
    "noise_interval": 3,     # Phase 4: insert noise every N chars
    "noise_char": "~"        # Phase 4: noise character to insert
}
```

## Algorithm Phases

| Phase | Name | Status |
|-------|------|--------|
| 1 | Substitution | 🔲 Not started |
| 2 | Transposition | 🔲 Not started |
| 3 | Key-Dependent | 🔲 Not started |
| 4 | Noise Injection | 🔲 Not started |
| 5 | Wild Card | 🔲 Not started |

## Running the Project

bash
## Author

Leon.L — Year 9, 2026

## License

MIT License — see [LICENSE](LICENSE) for details.
