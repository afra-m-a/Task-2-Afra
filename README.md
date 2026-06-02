# Master Cipher Suite

A professional, modern cryptographic tool implementing symmetric key ciphers with a polished Graphical User Interface (GUI). Includes an automated cryptoanalysis engine capable of cracking Caesar ciphers using frequency heuristic scoring.

## Features

- **Caesar Cipher** – Implements character rotation logic ($E_n(x) = (x + n) \pmod{26}$) while flawlessly preserving case, spaces, numbers, and punctuation.
- **Vigenère Cipher** – Polyalphabetic substitution using a repeating alphabetic keyword to mitigate single-frequency vulnerabilities. Non‑alphabetic key characters are cleanly ignored.
- **Automated Cryptoanalysis** – An intelligent analytical tool that brute-forces all 25 Caesar shifts, automatically scoring text structure against high-frequency English markers (`the`, `and`, `ing`, `tion`, etc.) to predict the correct key.
- **Modern GUI Application** – Designed with a dark-mode theme utilizing `customtkinter`:
  - **Encrypt / Decrypt Hub:** Real-time field switching based on selected algorithm (integer keys vs. text strings).
  - **Cryptoanalysis Sandbox:** One-click utility to break captured ciphertext and extract plaintexts.
  - One-click copy-to-clipboard integrations across all terminal dashboards.

---

## Project Architecture

```text
cipher_suite/
├── ciphers.py          # Core Cryptographic Engines (Caesar & Vigenère classes)
├── analyzer.py         # Cryptoanalysis / Automated Frequency Cracker
├── gui.py              # Front-end Interface Application (customtkinter layout)
├── main.py             # Global execution gateway 
└── README.md           # Documentation

```

---

## Installation & Environment Setup

1. **Clone or download** this repository to your workspace folder.
2. Ensure you have **Python 3.7+** installed.
3. Open your terminal inside the project directory and initialize your environment dependencies:

```bash
pip install customtkinter

```

> **Note for Linux Users:** If you encounter display errors, ensure your system's underlying Tk interprocess communication wrapper is installed:
> ```bash
> sudo apt install python3-tk
> 
> ```
> 
> 

---

## Usage Instructions

To launch the full visual suite, execute the main module from your terminal window:

```bash
python main.py

```

### 1. Encryption / Decryption Module

* Toggle between **Caesar** or **Vigenère** modes.
* Select your execution track (**Encrypt** or **Decrypt**).
* Enter your raw input payload.
* Provide a relevant key profile:
* *Caesar parameter:* An integer shift matrix (e.g., `3`).
* *Vigenère parameter:* An alphabetical password string (e.g., `secret`).


* Select **Execute** to capture output transformations immediately.

### 2. Cryptoanalysis Tool (Caesar Cracker)

* Navigate to the **Cryptoanalysis** workspace panel.
* Paste any obfuscated Caesar ciphertext string into the capture zone.
* Click **Crack Message**.
* The engine will programmatically deduce the shift offset, print the metrics, and dump the restored cleartext payload.

---

## Standard Execution Verification

### Caesar Cipher Profile

* **Plaintext:** `Hello, World!`
* **Shift Matrix:** `3`
* **Ciphertext Result:** `Khoor, Zruog!`

### Vigenère Cipher Profile

* **Plaintext:** `Attack at dawn`
* **Keyword Matrix:** `lemon`
* **Ciphertext Result:** `Lxfopv at lzgw`

### Heuristic Cracking Validation

* **Target Ciphertext:** `Wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj`
* **Calculated Metrics:** `Most likely key: 3`
* **Restored Plaintext:** `The quick brown fox jumps over the lazy dog`
