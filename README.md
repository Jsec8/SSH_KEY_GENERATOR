# SSH Key Generator

SSH Key Generator is a simple Python script to generate SSH key pairs (RSA or DSA) with optional password protection.

## Features

- Supports RSA and DSA key generation.
- Allows specifying the key size (1024, 2048, or 4096 bits).
- Optional passphrase for securing the private key.
- Saves the keys in the default SSH directory (`~/.ssh`).

## Requirements

- Python 3.6+
- `paramiko` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Jsec8/ssh-key-generator.git
    cd ssh-key-generator
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## Usage

Run the script:

```bash
python ssh_key_generator.py
