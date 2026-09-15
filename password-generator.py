# садыков

import secrets
import string


def get_yes_no(prompt: str) -> bool:
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes", "д", "да", ""):
            return True
        if answer in ("n", "no", "н", "нет"):
            return False
        print("Пожалуйста, ответьте 'y' (да) или 'n' (нет).")


def get_length() -> int:
    while True:
        raw = input("Введите желаемую длину пароля (например, 16): ").strip()
        try:
            length = int(raw)
        except ValueError:
            print("Ошибка: нужно ввести целое число.")
            continue
        if length < 4:
            print("Слишком коротко. Минимальная длина — 4 символа.")
            continue
        if length > 256:
            print("Слишком длинно. Максимум — 256 символов.")
            continue
        return length


def build_charset() -> str:
    charset = ""
    if get_yes_no("Использовать строчные буквы (a-z)? [Y/n]: "):
        charset += string.ascii_lowercase
    if get_yes_no("Использовать прописные буквы (A-Z)? [Y/n]: "):
        charset += string.ascii_uppercase
    if get_yes_no("Использовать цифры (0-9)? [Y/n]: "):
        charset += string.digits
    if get_yes_no("Использовать спецсимволы (!@#$%^&*...)? [Y/n]: "):
        charset += string.punctuation
    return charset


def generate_password(length: int, charset: str) -> str:
    return "".join(secrets.choice(charset) for _ in range(length))


def main() -> None:
    length = get_length()
    charset = build_charset()

    if not charset:
        print("Вы не выбрали ни одной категории символов. Выход.")
        return

    password = generate_password(length, charset)

    print("\nСгенерированный пароль:")
    print(password)
    print(f"\nДлина: {len(password)}")
    print(f"Использовано символов из набора размером {len(charset)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрервано пользователем.")
