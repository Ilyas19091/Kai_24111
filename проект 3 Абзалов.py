import random
import string

length = int(input("Введите длину пароля: "))
use_letters = input("Нужны буквы? (да/нет): ")
use_digits = input("Нужны цифры? (да/нет): ")
use_special = input("Нужны спецсимволы? (да/нет): ")

all_chars = ""
password = []

if use_letters == "да":
    all_chars = all_chars + string.ascii_letters

if use_digits == "да":
    all_chars = all_chars + string.digits

if use_special == "да":
    all_chars = all_chars + string.punctuation

chosen_types = 0
if use_letters == "да": chosen_types += 1
if use_digits == "да": chosen_types += 1
if use_special == "да": chosen_types += 1

if length >= chosen_types:
    if use_letters == "да":
        password.append(random.choice(string.ascii_letters))
    if use_digits == "да":
        password.append(random.choice(string.digits))
    if use_special == "да":
        password.append(random.choice(string.punctuation))

remaining = length - len(password)
for i in range(remaining):
    password.append(random.choice(all_chars))

random.shuffle(password)
final_password = "".join(password)
print("Ваш пароль:", final_password)
