# pyright: reportMissingModuleSource=false

# Litzy Gabriella Carela    Sep 7, 2021
# Sales Tax V1.0,  Pgm 2-6
# Purpose: To find the annual profit from the projected amount of sales.

# Input(s):
# - Amount of Purchase

# Output(s):
# - State Sales Tax
# - County Sales Tax
# - Totals Sales Tax
# - Sale Total

# I'm going to install the tabulate library to make it look nicer when it is printed out as a receipt.
from tabulate import tabulate

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
countyTax = float(purchaseAmountString)*stateTaxPercent

salesTax = stateTax + countyTax

saleTotal = float(purchaseAmountString) + salesTax

receipt = [['Subtotal', 'State Sales Tax', 'County Tax', 'Total Sales Tax', 'Sales Total'], [purchaseAmount, stateTax, countyTax, salesTax, saleTotal]]
print(tabulate(receipt))

print('Thank you for your purchase. Hope you have a great rest of your day and we hope to see you again soon!')