import paramiko
import os

def generate_ssh_key(key_type="rsa", key_bits=2048, passphrase=None):
    # Genera un par de claves SSH
    if key_type.lower() == "rsa":
        key = paramiko.RSAKey.generate(bits=key_bits)
    elif key_type.lower() == "dsa":
        key = paramiko.DSSKey.generate(bits=key_bits)
    else:
        raise ValueError("Unsupported key type. Supported types: rsa, dsa")

    private_key = key
    public_key = f"{key.get_name()} {key.get_base64()}"

    return private_key, public_key

def save_key_to_file(private_key, public_key, key_name="id_rsa", passphrase=None):
    private_key_path = os.path.expanduser(f"~/.ssh/{key_name}")
    public_key_path = f"{private_key_path}.pub"

    os.makedirs(os.path.dirname(private_key_path), exist_ok=True)

    # Guardar clave privada con o sin contraseña
    private_key.write_private_key_file(private_key_path, password=passphrase)

    with open(public_key_path, "w") as pub_file:
        pub_file.write(public_key)

    os.chmod(private_key_path, 0o600)

    print(f"Private key saved to: {private_key_path}")
    print(f"Public key saved to: {public_key_path}")

    # Validar que la clave privada se guarda correctamente con la contraseña
    try:
        if private_key.get_name() == "ssh-rsa":
            paramiko.RSAKey(filename=private_key_path, password=passphrase)
        elif private_key.get_name() == "ssh-dss":
            paramiko.DSSKey(filename=private_key_path, password=passphrase)
        print("Password protection is correctly applied.")
    except paramiko.ssh_exception.PasswordRequiredException:
        print("Password protection is not correctly applied.")

def main():
    print("SSH Key Generator")
    print("=================")

    key_type = input("Enter key type (rsa/dsa): ").strip().lower()
    key_bits = int(input("Enter key bits (1024/2048/4096): ").strip())
    passphrase = input("Enter passphrase (leave empty for no passphrase): ").strip() or None

    # Establecer el nombre predeterminado basado en el tipo de clave
    default_key_name = f"id_{key_type}"
    key_name = input(f"Enter key name (default: {default_key_name}): ").strip() or default_key_name

    private_key, public_key = generate_ssh_key(key_type=key_type, key_bits=key_bits, passphrase=passphrase)
    save_key_to_file(private_key, public_key, key_name=key_name, passphrase=passphrase)

if __name__ == "__main__":
    main()
















