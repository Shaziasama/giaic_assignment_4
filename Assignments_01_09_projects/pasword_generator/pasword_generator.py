#project 6
#password generator in python

import random
import string

def generate_password(length=12):
    # Define the character 
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(length))
    return password

#users inputs
length = int(input('Enter the length of the password: '))

password = generate_password(length)

print('Generated password:', password)