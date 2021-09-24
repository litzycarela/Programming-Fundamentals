# Litzy Gabriella Carela    Sep 23, 2021
# Population Calculator V1.0,  Pgm 4-13
# Purpose: Finding the projected population of organisms

# Input
# - Starting number of organisms (org)
# - Daily percentage increase (increase)
# - Number of days (days)

# Output
# - A table with days and the organism population number

# Named Constants
ONE = 1
ROUND = 3  # Rounding Number
PER = 100  # Number used for making the percentage

while True:
    # Welcome Statement
    print("Hello! This program will show you average daily population increase of organisms.")

    # inputs
    while True:  # Input Validation Check
        try:
            org: int = int(input("Starting number of organisms: "))
            break
        except ValueError:
            print("Please give me an integer")
    increase = float(input("Average daily increase (%): ")) / PER

    while True:  # Input Validation once again
        try:
            days = range(int(input("Number of days: ")))
            break
        except ValueError:
            print("Try again please! Please give me an whole number of days")

    # Here it will calculate the total population based on the number of days and output it
    table = list(map(lambda x: round(org * (ONE + increase) ** days.index(x), ROUND), days))
    print("\nDays\t Approximate Population")

    for increase, amount in enumerate(table, ONE):
        print(f"{increase:^4}\t{amount:^22}")
# Below this loop will give the users the option to start everything over again!
    if input('Would you like to calculate a new organism population? (yes or no) ').lower() == 'yes':
        continue
    else:
        print('Thanks for using this program! Have a good day!')  # End statement!
        break
