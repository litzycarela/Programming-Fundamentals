# Litzy Gabriella Carela    Sep 23, 2021
# Name Here V1.0,  Pgm 4-12
# Purpose: 

# Input(s):
# - positive number (num)

# Output(s):
# - Factorial

# Named Constants
factorial = 1
zero = 0
first = 1

# Welcome Statement
print('Welcome! Here you can calculate the factorial of any positive number!')

while True:
    num = int(input('Please enter a positive whole number: '))
    if num < zero:
        print('Oops that\'s not right! Please enter a whole number that is greater than 0: ')
        continue  # If they give the wrong input it will send them back
    for factoring in range(first, num+first):
        factorial *= factoring
        print("Thanks for the info! The factorial of", num, "is", factorial)

    if input('Would you like to enter another number? (yes or no)').lower() == "yes":
        continue
    else:
        print("Hope you found this program helpful!")
        break
