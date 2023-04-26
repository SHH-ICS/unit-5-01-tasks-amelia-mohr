# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.

import math
import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
finished = False 
while not finished:
    try:
        a = float(input("Please enter a length for leg a of your triangle: "))
        if a <= 0:
            raise ValueError
        b = float(input("Please enter a length for leg b of your triangle: "))
        if b <= 0:
            raise ValueError
        u = str(input("Please enter a unit (ex. cm, ft, etc.): "))
        firstc = (a**2) + (b**2)
        secondc = math.sqrt(firstc)
        c = round(decimal.Decimal(str(secondc)), 2)
        print("All results are rounded to 2 decimal places.")
        print("The hypotenuse of your triangle is: " + str(c) + " " + u)
        finished = True
    except ValueError:
        print("Please enter a POSITIVE NUMBER!")
