# ShadowCrack

A lightweight, command-line cryptography tool built from scratch in Python. It allows you to quickly encrypt messages using a custom shift key or brute-force decrypt scrambled text by testing all 25 possible alphabet alignments simultaneously.

## Features

* **Dual-Case Support:** Seamlessly handles both uppercase and lowercase letters.
* **Punctuation Protection:** Safely preserves spaces, numbers, and special characters (`!`, `?`, `.`, etc.) without distorting them.
* **Brute-Force Cracking:** Decrypts text without knowing the key by listing every single mathematical possibility side-by-side.
* **Interactive CLI Menu:** Clean, formatted interface with error fallback for invalid inputs.

---

## Installation

1. **Clone the repository** (or simply copy the script file):

   ```bash
   git clone https://github.com/wiz33better/ShadowCrack/
   cd ShadowCrack
   ```

2. **Prerequisites:** Make sure you have Python 3 installed. You can check by running:

   ```bash
   python --version
   ```

   (No external dependencies or libraries are required to run this tool!)

## How to Use?

Run the script from your terminal:

```bash
python main.py
```

**Options:**

* **Encrypt (E):** Enter your secret message and choose a shift value between 1 and 25 to generate an encoded string.
* **Decrypt (D):** Paste an encoded message. The toolkit will print out 25 rows (one for each possible shift key). Scan the list to find the row that reads in clear English.
* **Quit (Q):** Safely exit the toolkit application.
