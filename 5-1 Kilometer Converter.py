# Litzy Gabriella Carela    Sep 28, 2021
# Kilometer Converter V1.0,  Pgm 5-1
# Purpose: Convert Kilometers into Miles

# Input
# - Distance in Kilometers (km)

# Output
# - Miles (m)

# Named Constants
KM2M = 0.6214

# Welcome Statement
print("Hello user! The purpose of this program is to convert Kilometers to Miles.")

# While loop to give users the option to restart and calculate another km value
while True:
    # Input Statement
    km_input = str(input("Please enter kilometers here: "))

    # This is a loop that will have input validation so if the user inputs any characters that are a comma or a space it
    # will ignore them and put the other characters in the empty string (km_string).
    km_string = ""
    for n in range(len(km_input)):
        if km_input[n] == ',' or km_input[n] == ' ':
            continue
        else:
            km_string += km_input[n]

# Here I make the string into a float for calculation purposes.
    km = float(km_string)

# Next are the conversions from Kilometers to miles
    m = km * KM2M

# Here is the output!
    print("Thank you for your input!", km, "kilometers =", f'{m:.3f}', "miles.")

# Below this loop will give the users the option to start everything over again!
    if input('Would you like to convert another value? (yes or no) ').lower() == 'yes':
        continue
    else:
        print('Thanks for using this program! Have a good day!')  # End statement!
        break