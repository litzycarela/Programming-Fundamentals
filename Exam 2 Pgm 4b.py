# Litzy Gabriella Carela, Nov 2, 2021
# Exam 2, Problem 4, Golf  Scores Display Part two

#Inputs
#  - None

# Outputs
# - Table of data from file

print('Welcome! This program will display golf scores from the file!')

def main():
    one = 1
    zero = 0
    two = 2
    try:
        golfScoreFile = open('golfRecords.txt', 'r')
    except IOError as errorGenerated:
        print("file not found.", errorGenerated)
    else:
        lineCount = one
        for line in golfScoreFile:
            golfRecLine = lineCount % two
            if golfRecLine == zero:
                print(line)
            if golfRecLine == one:
                print(line)
            lineCount = lineCount + one
        golfScoreFile.close()


main() #Call Main