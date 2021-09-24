# Litzy Gabriella Carela    Sep 7, 2021
# Sales Tax V1.0,  Pgm 2-6
# Purpose: To find the annual profit from the projected amount of sales.

# Input(org):
# - Amount of Purchase

# Output(org):
# - State Sales Tax
# - County Sales Tax
# - Totals Sales Tax
# - Sale Total

# Named Constants
# - STATE_TAX (0.05)
# - COUNTY_TAX (0.025)

# Gives a welcome message.
print('Welcome, user. This program is made to find your sales tax and sale total!')

# Input Message
purchaseAmount = str(input('Please input your purchase amount: $'))

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
stateTaxPercent = 0.05
stateTax = purchaseAmountFloat * stateTaxPercent

countyTaxPercent = 0.025
countyTax = purchaseAmountFloat * countyTaxPercent

salesTax = stateTax + countyTax

saleTotal = purchaseAmountFloat + salesTax


print('Thank you for your purchase. Hope you have a great rest of your day and we hope to see you again soon!')

# You may notice that for the strings it uses double quotes instead of single quotes. For some reason everytime I try to use single quotes (as per usual), I recieve an error message.
print(f'{"Subtotal: ":>12}', f'{"$":>10}', f'{purchaseAmountFloat:>10,.2f}', sep='')
print(f'{"State Tax: ":>12}', f'{"$":>10}', f'{stateTax:>10,.2f}', sep='')
print(f'{"County Tax: ":>12}', f'{"$":>10}', f'{countyTax:>10,.2f}', sep='')
print(f'{"Total Tax: ":>12}', f'{"$":>10}', f'{salesTax:>10,.2f}', sep='')
print(f'{"Sale Total: ":>12}', f'{"$":>10}', f'{saleTotal:>10,.2f}', sep='')