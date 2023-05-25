import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_list = []
l_letters = len(letters) - 1
l_numbers = len(numbers) - 1
l_symbols = len(symbols) - 1

for i in range(0, nr_letters):
    pass_list.append(letters[random.randint(0, l_letters)])

for i in range(0, nr_symbols):
    pass_list.append(symbols[random.randint(0, l_symbols)])

for i in range(0, nr_numbers):
    pass_list.append(numbers[random.randint(0, l_numbers)])


uzunluk = nr_letters + nr_numbers + nr_symbols
uzun_list = []
gecici = []

for i in range(0, 100):
    if len(uzun_list) == uzunluk:
        break
    item = random.randint(0, uzunluk - 1)

    if item not in uzun_list:
        uzun_list.append(item)
        continue

for i in uzun_list:
    number = uzun_list[i]
    gecici.append(pass_list[number])

password = ''.join(gecici)
print(password)

