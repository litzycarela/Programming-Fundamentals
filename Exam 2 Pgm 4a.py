# Litzy Gabriella Carela, Nov 2, 2021
# Exam 2, Problem 4, Golf  Scores Display Part one

#Inputs
# - Player Name
# - Player Score
# - Ability to add new player

# Outputs
# - N/A in Part a

def main(): #main function
    while True:
        player, score = inputs()
        formats(player, score)
        fPlayer_name, fPlayer_score = formats(player, score)
        data_record(fPlayer_name, fPlayer_score)
        if input("Is everything alright or do you want to enter a "
                 "another player? [y or n} ").lower() == "y":  # rerun loop
            continue
        else:
            print("thank you for using this program ")  # end statement
            break


def inputs():
    player = (input("Enter the player's name: "))  # input player name

    while True:
        try:
            score = float(input("Enter the player's score: "))
            break
        except ValueError:  # Value Error
            print("Please only give me a number! ")

    return player, score


def formats(player, score):  # Formatting block
    fPlayer_name = str(format(player))
    fPlayer_score = str(format(score))

    return fPlayer_name, fPlayer_score


def data_record(fPlayer_name, fPlayer_score):  # Writing in the file
    golfScoreFile = open('golfRecords.txt', 'a')
    golfScoreFile.write("{0:<10}".format(fPlayer_name) + "{0:>10}".format(fPlayer_score + "\n"))
    golfScoreFile.close()


main()