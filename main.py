import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PassWord Generator")
numcount = 0
letcount = 0
symcount = 0
password = []
num_letters = int(input(f"How many letters would you like in your password? "))
num_numbers = int(input(f"How many numbers would you like in your password? "))
num_symbols = int(input(f"How many symbols would you like in your password? "))

while letcount <= num_letters - 1:
    letter = (random.choice(letters))
    letcount += 1
    password.append(letter)
print(password)
while numcount <= num_numbers - 1:
    number = (random.choice(numbers))
    numcount += 1
    password.append(number)
print(password)
while symcount <= num_symbols - 1:
    symbol = (random.choice(symbols))
    symcount += 1
    password.append(symbol)
print(password)
