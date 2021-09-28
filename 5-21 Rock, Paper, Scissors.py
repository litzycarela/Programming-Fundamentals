# Litzy Gabriella Carela    Sep 28, 2021
# Rock, Paper, Scissors V1.0,  Pgm 5-21
# Purpose: Play rock, paper, scissors!

# Input
# - rock paper or scissors (weapon_input)

# Output
# - Whether you win or lose

# Named Constants
import random
while True:
    # Welcome Message
    print("Welcome to DOOM")

    # Input message
    weapon_input = input("CHOOSE YOUR WEAPON (rock, paper, scissors): ")

    # Here the computer can randomly pick whether it wants rock, paper, or scissors
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    # Next is the outputs!
    print(f"You chose {weapon_input}, your opponent has attacked with {computer}.\n")
    if weapon_input == computer:
        print(f"Both players selected {weapon_input}. It's a tie! To break the tie you must play again.")
        continue
    elif weapon_input == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif weapon_input == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif weapon_input == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
        # Below this loop will give the users the option to start everything over again!
    if input('Would you like experience DOOM once again? (yes or no) ').lower() == 'yes':
        continue
    else:
        print('Thanks for playing DOOM! Have a good day!')  # End statement!
        break
