# Litzy Gabriella Carela    Sep 23, 2021
# Name Here V1.0,  Pgm 4-13
# Purpose: 

# Input(s):
# - Starting number of organisms (s)
# - Daily percentage increase (i)
# - Number of days (d)

# Output(s):
# - A table with days and the organism population number

# Named Constants
ONE = 1
ROUND = 3  # Rounding Number
DIV = 100  # Number for Division

while True:
    # Welcome Statement
    print("Hello! This program will show you average daily population increase of organisms.")

    # inputs
    while True:  # Input Validation Check
        try:
            s: int = int(input("Starting number of organisms: "))
            break
        except ValueError:
            print("Please give me an integer")
    i = float(input("Average daily increase[%]: ")) / DIV

    while True:  # Input Validation once again
        try:
            d = range(int(input("Number of days to multiply: ")))
            break
        except ValueError:
            print("Please give me an exact number of days")

    # Calculation & output
    Sum = list(map(lambda x: round(s * (ONE + i) ** d.index(x), ROUND), d))
    print("\nDays\t Approximate Population")

    for i, amount in enumerate(Sum, ONE):
        print(f"{i:^4}\t{amount:^22}")
# Below this loop will give the users the option to start everything over again!
    if input('Would you like to calculate a new organism population? (yes or no) ').lower() == 'yes':
        continue
    else:
        print('Thanks for using this program! Have a good day!')  # End statement!
        break
