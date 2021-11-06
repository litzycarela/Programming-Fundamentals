# Litzy Gabriella Carela    Nov 2, 2021
# Random Number Generator Game,  Exam 2 Pgm 3
# Purpose: Write a program that generates a random number 
# and asks the user to guess what the number is.

# Input:
# - Number

# Output:
# - Too High, Too Low, Congrats, or Value Error

#imports
import random

def welcome():
    name = input('Who has chosen to step forth and commence THE GAME? (input name here): ')
    print('Hey', name ,'and welcome to THE GAME where you input a number and we tell you if your right or wrong!')

# Variables
start = 1 # this is for the range from 1-100
end = 100


def main(): # this function is for the input statements
    while True:
        try:
            num = int(input('To play, please enter a number from 1-100: '))
            break
        except ValueError:
            print('Hey there! Please make sure you entered a whole number and try again.')
    calc(num)


def calc(guess):
    rand_num = random.randrange(start, end) # this genereates a random number within 1 and 100
    error = False
    while True:
        if not error:
            if guess > rand_num: #in case a number is too high it will give this hint
                print('Too high, try again.')
            elif guess < rand_num: #in case a number is too low it will give this hint
                print('Too low, try again.')
            elif guess == rand_num:
                continue
        error = False
        try:
            guess = int(input('What\'s your new guess?: '))

            if guess == rand_num:
                print('Congratulations! You guessed correctly!')
                if guess == rand_num:
                    loop = input('You guessed correctly! Want to play again (y or n)? ')
                    if loop == 'y':
                        rand_num = random.randrange(1, 100)
                        error = True
                        continue
                    else:
                        print("Thank you for playing! Have a good day and I'll see you soon!")
                        break
        except ValueError:
            error = True
            print('Hey there! Please make sure you entered a number and try again.')

welcome()
main()