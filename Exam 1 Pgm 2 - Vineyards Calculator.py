# Litzy Gabriella Carela    Sep 17, 2021
# Vineyard Owner V1.0,  Exam 1 Pgm 2
# Purpose: To calculate the number of grapevines to plant in each row.

# Input(s):
# - Name (this isn't requiered but as a user always feels nice when they use your name in a program :) )
# -- variable is "user"
# - Length of the Row (rowInput)
# - Amount of Space used by End-Post Assembly (endpost)
# - Amount of Space between Vines (space)


# Output(s):
# - The number of grapevines per row (vines)

# Named Constants
TWO = 2

# Equation is Vines = ((row-2)*endpost space)/space between vines
# Can also be displayes as vines = (((row - TWO) * endpost) / space)

# Our output has to be an integer but we don't want to round so we will have to import math to use the truncate function to eliminate the decimals without rounding up.
import math

# Gives a welcome message.
user = input("Hi there! What's your name? ")
print('Welcome', user, '. This program is made to find out how many grapevines will fit in each row!')

# Input Message
row = float(input('Please enter the row length in feet: '))
# Normally input validation would go here but thanks to Dr.Daniels generous assumption on perfect inputs we get to skip that!

# Below I'll ask for the endpost assembly space used and the space between vines
endpost = float(input('Please input the space taken up by End-Post Assembly (no commas): '))
space = float(input('Please input the space between each vine (no commas): '))

# Next we can use the formula to find the number of vines per row
# We will also use the truncate function to round down and take away the decimal points
vines = math.trunc((((row - TWO) * endpost) / space))

# Now a print and end statement!
print('Thank you for using this calculator! You can place', vines, 'grapevines in each row. Have a great day!')