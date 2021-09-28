# Litzy Gabriella Carela    Sep 28, 2021
# Property Tax V1.0,  Pgm 5-5
# Purpose: Find the assessment value and property tax given a properties value

# Input
# - land value (land_value_input)

# Output
# - Assessment Value (av)
# - Property Tax (property_tax)

# Named Constants
PER_DOLLAR = 100
SEVENTY2 = 0.72
SIXTY_PERCENT = 0.6


def main():  # Main function
    print("Welcome user! This program will find the assessment value and property tax of a property.")
    print("Please make sure there are no commas.")
    lv = land_value()
    av = calculate_land_value(lv)
    property_tax = calculate_propertytax(av)
    print("The property's value entered is: $", f'{lv:>10,.2f}')
    print("The Assessment value is $", f'{av:>19,.2f}')
    print("The Property Tax is $", f'{property_tax:>23,.2f}')
    print("Thanks for using the Property Tax calculator!")


def land_value():  # Asking for land value
    land_value_input = float(input("Please enter the property's actual value: "))
    return land_value_input


def calculate_land_value(land_value_input):  # Function for calculation land value
    land_value_out = (SIXTY_PERCENT * land_value_input)
    return land_value_out


def calculate_propertytax(land_value_out):  # function for property tax
    property_tax = (land_value_out / PER_DOLLAR) * SEVENTY2
    return property_tax


main()
