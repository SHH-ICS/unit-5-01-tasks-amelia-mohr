# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.

import random
finished = False
while not finished:
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    try: 
        q = int(input("What is the answer to " + str(num1) + " + " + str(num2) + ": "))
    except ValueError:
        print("Please don't enter text!")
    if q == num1 + num2:
        print("Congratulations!! You are competent!")
        finished = True
    else: 
        print("Try again idiot (I say this with love).")