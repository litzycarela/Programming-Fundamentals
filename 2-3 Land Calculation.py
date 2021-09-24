# Litzy G. Carela    8/31/2021
# Land Calculator V1.0, Pgm 2-3 textbook
# Calculates total number of acres based on square footage
# Input(org)
#   Square Feet
#
# Output
#   Acres
#
# Formula for conversion is Acres = square feet of land /43,560)
#
print('Welcome to the acre calculator! So you want to know how many acres are in your plot of land? Leave it to me.')
sqft = float(input('Please input the total square footage of your plot of land here: '))
#the "a" variable stands for acres
a = (sqft/43560)
print('Thanks for the information! Your land is a total of', a, 'acres!') 
print('Thank you for using our square feet to acre calculator. If you find this useful feel free to leave us a review below!')