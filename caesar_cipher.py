SHIFT = 5


def encrypt(text: str, shift: int = SHIFT) -> str:
    encrypted_text = ""

    for char in text:
        encrypted_text += chr((ord(char) + shift) % 65536)

    return encrypted_text


def decrypt(text: str, shift: int = SHIFT) -> str:
    decrypted_text = ""

    for char in text:
        decrypted_text += chr((ord(char) - shift) % 65536)

    return decrypted_text


def main() -> None:
    password = input("Введите пароль: ")

    encrypted_password = encrypt(password)
    print("Зашифрованный пароль:", encrypted_password)

    decrypted_password = decrypt(encrypted_password)
    print("Расшифрованный пароль:", decrypted_password)


if __name__ == "__main__":
    main()