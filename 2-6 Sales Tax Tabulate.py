from tabulate import tabulate
#  Litzy Gabriella Carela    Sep 7, 2021
# Sales Tax V1.0,  Pgm 2-6
# Purpose: To find the annual profit from the projected amount of sales.

# Input:
# - Amount of Purchase

# Output:
# - State Sales Tax
# - County Sales Tax
# - Totals Sales Tax
# - Sale Total

# I'm going to install the tabulate library to make it look nicer when it is printed out as a receipt.


# Gives a welcome message.
print('Welcome, user. This program is made to find your sales tax and sale total!')

# Input Message  and explanation for calculations below
purchaseAmount = str(input('Please input your purchase amount: $'))
purchaseAmountString = ""
for n in range(len(purchaseAmount)):
    if purchaseAmount[n] == ',' or purchaseAmount[n] == ' ':
        continue
    else:
        purchaseAmountString += purchaseAmount[n]

# Calculations here
stateTaxPercent = 0.05
stateTax = float(purchaseAmountString)*stateTaxPercent

countyTaxPercent = 0.025
countyTax = float(purchaseAmountString)*countyTaxPercent

salesTax = stateTax + countyTax

saleTotal = float(purchaseAmountString) + salesTax

receipt = [['Subtotal', f'{float(purchaseAmount):,.2f}'], ['State Sales Tax', f'{float(stateTax):,.2f}'], ['County Tax', f'{float(countyTax):,.2f}'], ['Total Sales Tax', f'{float(salesTax):,.2f}'], ['Sales Total', f'{saleTotal:,.2f}']]
print(tabulate(receipt))

print('Thank you for your purchase. Hope you have a great rest of your day and we hope to see you again soon!')