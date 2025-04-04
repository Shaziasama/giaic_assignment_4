#project 3 Guess the Number Game python project(User)

import random
#generate a random number
number = random.randint(1, 100)
print("Guess the number between 1 and 100! ")

while True:
    user_number = int(input("Enter a number between 1 and 100: "))
    if user_number == number:
        print("Congratulations! You won.")
        break
    elif user_number > number:
        print("Try a smaller number.")
    else:
        print("Try a larger number.")