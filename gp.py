import random
print('Да начнется веселье!!')
digits = "0123456789" # цифры
lowercase_letters = "abcdefghijklmnopqrstuvwxyz" # маленькие буквы
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
bad_punctuation = "il1Lo0O"

chars = ""

total_pass = int(input("Укажите количество паролей ").strip())
len_pass = int(input("Укажите длину пароля ").strip())
dig_pass = input("Включать ли цифры? да или нет ").strip()
up_pass = input("Включать ли прописные буквы? да или нет ").strip()
low_pass = input("Включать ли строчные буквы? да или нет ").strip()
punc_pass = input("Включать ли символы? да или нет ").strip()
bad_punc_pass = input("Исключить неоднозначные символы? да или нет ").strip()


if dig_pass.lower() == "да":
    chars += digits
if up_pass.lower() == "да":
    chars += uppercase_letters
if low_pass.lower() == "да":
    chars += lowercase_letters
if punc_pass.lower() == "да":
    chars += punctuation
if bad_punc_pass == "да":
    for i in "il1Lo0O":
        chars = chars.replace(i, "")


def generate_password(len_pass, chars):
    password = ""
    for j in range(len_pass):
        password += random.choice(chars)
    return password


for _ in range(total_pass):
    print(generate_password(len_pass, chars), sep="\n")
