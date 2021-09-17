# Litzy Gabriella Carela    Sep 17, 2021
# Vineyard Owner V1.0,  Exam 1 Pgm 2
# Purpose: To calculate the number of grapevines to plant in each row.

# Input(s):
# - Name (this isn't requiered but as a user always feels nice when they use your name in a program :) )
# -- variable is "user"
# - Length of the Row (rowInput)
# - Amount of Space used by End-Post Assembly (endpostInput)
# - Amount of Space between Vines (spaceInput)


# Output(s):
# - The number of grapevines per row (vines)

# Named Constants
TWO = 2

# Our output has to be an integer but we don't want to round so we will have to import math to use the truncate function to eliminate the decimals without rounding up.
import math

# Gives a welcome message.
user = input("Hi there! What's your name?")
print('Welcome', user, '. This program is made to find out how many grapevines will fit per row!')

# Input Message
rowInput = str(input('Please enter the row length in feet: '))
# I looked up how long the average row in a vineyard is in feet and lets just say... THEY'RE BIG (up to 700) so we'll put some input validation just in case it goes to the thousands.
# This is a loop that will have input validation so if the user inputs any characters that are a comma or a space it will ignore them and put the other characters in the empty string (purchaseAmountString).
rowString = ""
for n in range(len(rowInput)):
    if rowInput[n] == ',' or rowInput[n] == ' ':
        continue
    else:
        rowString += rowInput[n]



#Here we make the string into a float that way it can be used in the next calculations.
row = float(rowString)