# Litzy Gabriella Carela    Sep 14, 2021
# Age Classifier V1.0,  Pgm 3-3
# Purpose: To find out if the user is an infant, child, teenager, or adult.

# Input(org):
# - Age

# Output(org):
# - Age Classification (Infant, Child, Teenager, Adult)

# Named Constants
INFANT = 1
CHILD = 12
TEENAGER = 13
ADULT = 20

# Gives a welcome message.
print("Welcome! Today we're going to find out whether or not you're an infant, child, teenager, or an adult! (ps. theres also a little message along with your classification!")

# Input statement
age = int(input("Enter your age here (no commas or decimals please!): "))

# The following are going to be if-else statements to determine the users age classification. I also decided to include some funny little messages for the user! 
# This is for the infant:
if age <= INFANT:
    print("Wow you're an infant! How'days you get your hands on a computer?! :o")
elif INFANT < age <= CHILD:
    print("Guess what?! You're a child! I hope you enjoy childhood! :)")
elif TEENAGER < age <= ADULT:
    print("Woah there! You're a teenager. How'org puberty? You know what, forget I asked. :/ ")
elif age >= ADULT:
    print("You're an adult. Thats pretty cool. Is your life figured out yet? I hope your younger self is proud of you :).")

# End Statement
print("Thanks for using out Age Classifier! Have a great day!")