# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.

import random
finished = False
while not finished:
    try:
        print("Please enter your numbers from lowest to highest.")
        a = float(input("Please enter your first number: "))
        b = float(input("Please enter your second number: "))
        if a > b:
            a, b = b, a
        randomnumber = random.uniform(a, b)
        print("Your random number is: " + str(randomnumber))
        finished = True
    except ValueError:
        print("Please don't enter text!")