# Litzy Gabriella Carela, Nov 2, 2021
# Exam 2, Problem 1, Future Value
# This program calculates a future value based on the input value.
#
# Import 
from matplotlib import pyplot as plt

# Input(s)
#   Present value of account
#   Monthly interest rate
#   Number of months

# Output(s)
#   Future value of account after specified time number of months

# Constants
one = 1
one_percent = 0.01

# Welcome Statements and purpose!
print('Welcome User! This program calculates future account value.')


def main():  # Main function
    input_one, input_two, input_three = user_inputs()  # Stating inputs
    calculations(input_one, input_two, input_three)  # Stating input calculations
    future_value = calculations(input_one, input_two, input_three)  # Stating future value

    output(future_value, input_one, input_three)  # Stating outputs


def user_inputs():  #Defining the main function
    while True:  # While loop for inputs
        try:
            input_one = (float(input('Please enter the present value of your account: ')))  # Present value input
            break
        except ValueError:
            print('Please make sure you entered a number and try again.')


    while True:
        try:
            input_two = (float(input('Please enter the monthly interest rate: ')))  # Monthly interest rate input
            break
        except ValueError:
            print('Please make sure you entered a number and try again.')

    while True:
        try:
            input_three = (float(input('Please enter the number of months: ')))  # Time span input
            break
        except ValueError:
            print('Please make sure you entered a number and try again.')

    return input_one, input_two, input_three


def calculations(input_one, input_two, input_three):
    future_value = input_one * (one + (one_percent * input_two)) ** input_three
    future_value = "$" + str(format(future_value, ".2f"))

    return future_value


def output(future_value, input_one, input_three):
    print("From your initial investment of:", input_one, "you will earn ", future_value, "in only this amount of months:", input_three, "months!")


main()