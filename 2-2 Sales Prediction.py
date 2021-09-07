# Litzy Gabriella Carela    Sep 7, 2021
# Salses Prediction V1.0,  Pgm 2-2
# Purpose: To find the annual profit from the projected amount of sales.

# Input(s):
# - Projected amount of total sales

# Output(s):
# - Profit

# Gives a welcome message.
print('Welcome, user. This program is made to find your businesses estimated annual profit! This is done by finding out the value of 23% of your estimated total sales.')

# Input Message  and explanation for calculations below
totalSales = str(input('Please input your projected amount of total sales: $'))
totalSalesString = ""
for n in range(len(totalSales)):
    if totalSales[n] == ',' or totalSales[n] == ' ':
        continue
    else:
        totalSalesString += totalSales[n]

# Calculations here
percent = 0.23
annualProfit = float(totalSalesString)*percent
print('Thanks for the information! Your projected amount of profit is a total of: $','{:,.2f}'.format(annualProfit), sep='')

# Gives an exit message.
print('Thank you for using our Profit Predictor. Hope your business continues to grow!')
