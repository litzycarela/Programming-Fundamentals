# Litzy Gabriella Carela    Sep 17, 2021
# Restaurant Meal V1.0,  Exam 1 Pgm 1
# Purpose: To calculate the tip, the tax, and the total for the meal purchased.

# Input(s):
# - Meal Charge

# Output(s):
# - Tip (foodTip)
# - Sales Tax (salesTax)
# - Sale Total (saleTotal)

# Named Constants
TIP_RATE=  0.15
TAX_RATE = 0.0825 

# Gives a welcome message.
print('Welcome, user. This program is made to find your meal total (with 15% tip included)!')

# Input Message
purchaseAmount = str(input('Please enter meal purchase amount: $'))

# This is a loop that will have input validation so if the user inputs any characters that are a comma or a space it will ignore them and put the other characters in the empty string (purchaseAmountString).
purchaseAmountString = ""
for n in range(len(purchaseAmount)):
    if purchaseAmount[n] == ',' or purchaseAmount[n] == ' ':
        continue
    else:
        purchaseAmountString += purchaseAmount[n]

#Here we make the string into a float that way it can be used in the next calculations.
purchaseAmountFloat = float(purchaseAmountString)

# Calculations here
foodTip = purchaseAmountFloat * TIP_RATE
salesTax = purchaseAmountFloat * TAX_RATE

saleTotal = purchaseAmountFloat + foodTip + salesTax


print('Thank you for your purchase. Hope you have a great rest of your day and we hope to see you again soon!')

# You may notice that for the strings it uses double quotes instead of single quotes. For some reason everytime I try to use single quotes (as per usual), I recieve an error message.
print(f'{"Subtotal: ":>12}', f'{"$":>10}', f'{purchaseAmountFloat:>10,.2f}', sep='')
print(f'{"Tip: ":>12}', f'{"$":>10}', f'{foodTip:>10,.2f}', sep='')
print(f'{"Sales Tax: ":>12}', f'{"$":>10}', f'{salesTax:>10,.2f}', sep='')
print(f'{"Sale Total: ":>12}', f'{"$":>10}', f'{saleTotal:>10,.2f}', sep='')