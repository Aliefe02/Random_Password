import random
import pyperclip

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'
size = random.randint(10,16)
password = ''

for i in range(size):
    password += random.choice(characters)

pyperclip.copy(password)