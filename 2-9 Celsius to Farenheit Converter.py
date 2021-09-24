# Litzy G. Carela    8/31/2021
# Convert CtoF  V1.0, Pgm 2-9 textbook
# Converts degrees of Celsius to Fahrenheit
# Input(org)
#   Celsius
#
# Output
#   Fahrenheit
#
# Formula for conversion is Celsius = ((9/5 * Celsius) + 32)
#
print('Hello there! Welcome to the Celsius to Farenheit conversion calculator. We hope that you find this helpful!')
C = float(input('Please input a Celsius temperature in degrees here: '))
F = ((9/5) * C + 32)
print( C, 'Celsius is equeal to', F, 'Fahrenheit') 
print('Thank you for using our conversion calculator. If you find this useful feel free to leave us a review below.')