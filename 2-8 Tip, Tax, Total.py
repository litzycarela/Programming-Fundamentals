# Litzy Gabriella Carela    Sep 7, 2021
# Sales Tax V1.0,  Pgm 2-8
# Purpose: To calculate the tip, the tax, and the total for the ordered food

# Input(org):
# - Amount of meal purchased

# Output(org):
# - Tip
# - Sales Tax
# - Sale Total

# Named Constants
# - TIP (0.18)
# - TAX (0.07)

# Gives a welcome message.
print('Welcome, user. This program is made to find your sales tax and sale total!')

# Input Message
purchaseAmount = str(input('Please enter meal purchase amount: $'))

# This is a loop that will have input validation so if the user inputs any characters that are a comma or a space it will ignore them and put the other characters in the empty string (purchaseAmountString).
purchaseAmountString = ""
for n in range(len(purchaseAmount)):
    if purchaseAmount[n] == ',' or purchaseAmount[n] == ' ':
        continue
    else:
        purchaseAmountString += purchaseAmount[n]

#
purchaseAmountFloat = float(purchaseAmountString)

# Calculations here
TIP = 0.18
foodTip = purchaseAmountFloat * TIP

TAX = 0.07
salesTax = purchaseAmountFloat * TAX

saleTotal = purchaseAmountFloat + foodTip + salesTax


print('Thank you for your purchase. Hope you have a great rest of your day and we hope to see you again soon!')

# You may notice that for the strings it uses double quotes instead of single quotes. For some reason everytime I try to use single quotes (as per usual), I recieve an error message.
print(f'{"Subtotal: ":>12}', f'{"$":>10}', f'{purchaseAmountFloat:>10,.2f}', sep='')
print(f'{"Tip: ":>12}', f'{"$":>10}', f'{foodTip:>10,.2f}', sep='')
print(f'{"Sales Tax: ":>12}', f'{"$":>10}', f'{salesTax:>10,.2f}', sep='')
print(f'{"Sale Total: ":>12}', f'{"$":>10}', f'{saleTotal:>10,.2f}', sep='')