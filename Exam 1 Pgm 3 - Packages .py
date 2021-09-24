# Litzy Gabriella Carela    Sep 17, 2021
# Shipping Costs V1.0,  Exam 1 Pgm 3
# Purpose: To calculate the shipping costs for each package

# Input(org):
# - Package Weight (pkg)

# Output(org):
# - shipping cost (cost)

# Named Constants
SMALL = 2     #packages that are 2 pounds or less
MEDIUM = 6    #packages that are greater than 2 lbs but less than or equal to 6 lbs
LARGE = 10    #packages that are greater than 6 lbs but less than or equal to 10 lbs
SRATE = 1.50  # rate for packages that are 2 pounds or less
MRATE = 3.00  # rate for packages that are greater than 2 lbs but less than or equal to 6 lbs
LRATE = 3.75  # rate for packages that are greater than 6 lbs but less than or equal to 10 lbs
XLRATE = 4.75 # rate for packages that are greater than 10 lbs

# Gives a welcome message.
print('Welcome to the shipping company. This program is made to find your package shipping costs based on how many pounds it weighs!')

while True: #this while loop will let us see if the user wants to ship another package or just leave it as is.
# Asks user for input!
    pkg = float(input('Please input package weight here: '))

# Now we're going to determine the rate for the package and calculate how much everything will cost!
    if pkg <= SMALL:
        cost = pkg * SRATE
        print('Thank you for the information! Your package weighs', pkg, 'lbs. This makes it eligible for our small package rate ($', SRATE, '/lb). Your total is:', '${:,.2f}'.format(cost))
    elif pkg <= MEDIUM:
        cost = pkg * MRATE
        print('Thank you for the information! Your package weighs', pkg, 'lbs. This makes it eligible for our medium package rate ($', MRATE, '/lb). Your total is:', '${:,.2f}'.format(cost))
    elif pkg <= LARGE:
        cost = pkg * LRATE
        print('Thank you for the information! Your package weighs', pkg, 'lbs. This makes it eligible for our large package rate ($', LRATE, '/lb). Your total is:', '${:,.2f}'.format(cost))
    elif pkg > LARGE:
        cost = pkg * XLRATE
        print('Thank you for the information! Your package weighs', pkg, 'lbs. This makes it eligible for our extra large package rate ($', XLRATE, '/lb). Your total is:', '${:,.2f}'.format(cost))

    if input('Would you like to ship another package?[yes or no] ').lower() == "yes":  # loop for yes or no
        continue
    else:
        print("Thank you for shipping with us!")  # end statement
        break