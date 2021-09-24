# Litzy Gabriella Carela    Sep 17, 2021
# Restaurant Meal V1.0,  Exam 1 Pgm 1
# Purpose: To calculate the tip, the tax, and the total for the meal purchased.

# Input(org):
# - Meal Charge

# Output(org):
# - Tip (foodTip)
# - Sales Tax (salesTax)
# - Sale Total (saleTotal)

# Named Constants
TIP_RATE=  0.15
TAX_RATE = 0.0825 

# Gives a welcome message.
print('Welcome, user. This program is made to find your meal total (with 15% tip included)!')

# Input Message
purchaseAmount = float(input('Please enter meal purchase amount: $'))

# Calculations here
foodTip = purchaseAmount * TIP_RATE
salesTax = purchaseAmount * TAX_RATE

saleTotal = purchaseAmount + foodTip + salesTax


print('Thank you for your purchase. Hope you have a great rest of your day and we hope to see you again soon!')

# You may notice that for the strings it uses double quotes instead of single quotes. For some reason everytime I try to use single quotes (as per usual), I recieve an error message.
print(f'{"Subtotal: ":>12}', f'{"$":>10}', f'{purchaseAmount:>10,.2f}', sep='')
print(f'{"Tip: ":>12}', f'{"$":>10}', f'{foodTip:>10,.2f}', sep='')
print(f'{"Sales Tax: ":>12}', f'{"$":>10}', f'{salesTax:>10,.2f}', sep='')
print(f'{"Sale Total: ":>12}', f'{"$":>10}', f'{saleTotal:>10,.2f}', sep='')