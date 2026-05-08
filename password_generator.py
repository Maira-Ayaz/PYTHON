import random

# Character sets
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

# User input
length = int(input("Enter password length: "))

use_letters = input("Include letters? (y/n): ").lower()
use_numbers = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()

# Create pool
pool = ""

if use_letters == "y":
    pool += letters

if use_numbers == "y":
    pool += numbers

if use_symbols == "y":
    pool += symbols

# Validation
if pool == "":
    print("Error: No character types selected!")
else:
    password = ""

    for i in range(length):
        password += random.choice(pool)

    print("Generated Password:", password)