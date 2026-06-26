# 🔐 RSA Encryption System

A simple RSA encryption and decryption system built with Python, featuring both a CLI and a graphical user interface (GUI).

---

## 📸 Preview

> A dark-themed GUI built with `tkinter` that lets you encrypt and decrypt messages using RSA keys generated in real time.

---

## 📁 Project Structure

```
RSA Encryption System/
├── rsa_core.py   # Core RSA algorithm (key generation, encrypt, decrypt)
├── utils.py      # Helper functions for terminal output
├── main.py       # Command-line interface (CLI)
└── gui.py        # Graphical user interface (GUI) with tkinter
```

---

## ⚙️ How It Works

RSA is an asymmetric encryption algorithm based on the mathematical difficulty of factoring large numbers.

1. Two random prime numbers `p` and `q` are generated
2. `n = p × q` is computed as the modulus
3. `φ(n) = (p-1)(q-1)` is calculated
4. Public key `e` is chosen such that `gcd(e, φ(n)) = 1`
5. Private key `d` is computed as the modular inverse of `e`

**Encryption:** `C = M^e mod n`  
**Decryption:** `M = C^d mod n`

---

## 🚀 Getting Started

### Requirements

- Python 3.x
- `tkinter` (included with Python by default)

### Run the GUI

```bash
python gui.py
```

### Run the CLI version

```bash
python main.py
```

---

## 🧪 Example Output

```
Input:     nima aslani
Public Key:  (7, 29503)
Private Key: (16663, 29503)
Encrypted:   26599 25859 8162 4440 13514 ...
Decrypted:   nima aslani
Result:      ✅ Success
```

---

## 🛠️ Built With

- **Python 3**
- **tkinter** — GUI library
- **No third-party libraries** — pure Python implementation

