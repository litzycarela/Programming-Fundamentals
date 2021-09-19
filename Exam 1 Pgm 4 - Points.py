# Litzy Gabriella Carela    Sep 17, 2021
# Bookstore Points V1.0,  Exam 1 Pgm 4
# Purpose: To calculate the number of points given for each book purchase

# Input(s):
# - number of books purchased (books)

# Output(s):
# - Amount of points awarded (pts)

# Named Constants
PT0 = 0   # 0 POINTS
PT2 = 5   # 5 POINTS
PT4 = 15  # 15 POINTS
PT6 = 30  # 30 POINTS
PT8 = 60  # 60 POINTS
BK2 = 2   # 2 BOOKS
BK4 = 4   # 4 BOOKS
BK6 = 6   # 6 BOOKS
BK8 = 8   # 8 BOOKS

#Welcome and input message
while True:
    try:
        books = int(input('Welcome to Python Forever! How many books will you purchasing with us today?'))
        break
    except ValueError:
        print("You can't buy part of a book silly! Please give me a whole number. (1,2,3,4,etc)")

# program deciding what points you are awarded
if books < BK2:
    print('The number of points you are awarded is', PT0, 'points!')
    print('Thank you for your business and we hope to see you again soon!')
elif BK4 > books >= BK2:
    print('The number of points you are awarded is', PT2, 'points! Congratulations.')
    print('Thank you for your business and we hope to see you again soon!')
elif BK6 > books >= BK4:
    print('The number of points you are awarded is', PT4, 'points! Congratulations.')
    print('Thank you for your business and we hope to see you again soon!')
elif BK8 > books >= BK6:
    print('The number of points you are awarded is', PT6, 'points! Congratulations.')
    print('Thank you for your business and we hope to see you again soon!')
elif books <= BK8:
    print('The number of points you are awarded is', PT8, 'points! Congratulations.')
    print('Thank you for your business and we hope to see you again soon!')