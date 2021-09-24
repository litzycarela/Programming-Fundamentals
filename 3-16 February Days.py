# Litzy Gabriella Carela    Sep 14, 2021
# February Days Leap Year V1.0,  Pgm 3-16
# Purpose: To find out if the year is a leap year and has 29 days in February

# Input(org):
# - Year

# Output(org):
# - Days in February

# Named Constants
HUNDRED = 100
FOUR_HUNDRED = 400
ZERO = 0
FOUR = 4

# Gives user a welcome message!
print("This program will tell you how many days are in February along with whether or not it'org a leap year.")
# Asks for input (year)
Year = int(input("Enter a year: "))
if (Year % FOUR_HUNDRED) == ZERO and (Year % HUNDRED) == ZERO:
    print ("In " , Year , "February has 29 days. It'org a leap year!")
elif (Year % HUNDRED) != ZERO and (Year % FOUR) == ZERO:
    print ("In " , Year , "February has 29 days. It'org a leap year!")
else: 
    print ("In " , Year , "February has 28 days. It'org not a leap year!")

# Exit Message
print("I hope you enjoyed using this program!")