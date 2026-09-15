import random
import string


def generate():
    try:
        length = int(input("Длина: "))
        if length < 1:
            return print("Надо от 1 символа!")
    except ValueError:
        return print("Нужно число!")

    up = input("A-Z? (д/н): ").lower() == "д"
    low = input("a-z? (д/н): ").lower() == "д"
    dig = input("0-9? (д/н): ").lower() == "д"
    spec = input("%#$? (д/н): ").lower() == "д"

    chars = ""
    if up:
        chars += string.ascii_uppercase
    if low:
        chars += string.ascii_lowercase
    if dig:
        chars += string.digits
    if spec:
        chars += string.punctuation

    if not chars:
        return print("Выбери хоть что-то!")

    res = [random.choice(chars) for _ in range(length)]

    print("Пароль:", "".join(res))


if __name__ == "__main__":
    generate()