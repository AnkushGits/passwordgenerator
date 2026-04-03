import random
import string

#take length using int input
length = int(input("Enter length: "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

#combine all
all_characters = letters + digits + symbols

password = ""

for i in range(length):
    password +=  random.choice(all_characters)

print(password)