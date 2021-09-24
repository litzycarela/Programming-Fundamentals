# Litzy Gabriella Carela    Sep 23, 2021
# Tuition Increase V1.0,  Pgm 4-10
# Purpose: Displays projected semester tuition amount for the next 5 years.

# Input
# - Tuition (however we were already given the tuition amount of $800 so no input)

# Output
# - projected semester tuition amount for the next 5 years

# Named Constants
CTUITION = 8000.00
TRATE = 1.03
ROUND = 1

# Welcome statement
print('Hi there! This is the tuition increase for the next 5 years based on an initial $', CTUITION, 'tuition.')
# This is the loop that will find the tuition increase for the next 5 years
for count in range(1, 6):
    print('The tuition cost for spring semester', count, 'is', '${:.2f}'.format(CTUITION, '<4'))
    print()
    CTUITION = round(CTUITION * TRATE, ROUND)
# This is the output statement
    print('The tuition cost for fall semester', count, 'is', '${:.2f}'.format(CTUITION, '>8'))
# Lastly when the loop finishes it will print out a good-bye/thank you message
if range(6):
    print()
    print('Thank you for using our tuition calculator.')
