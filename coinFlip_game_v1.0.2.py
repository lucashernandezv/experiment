import random
import sys


def create_players():
    global player1
    global player2

    print ("[Player 1]")
    player1 = str.lower(raw_input("Type in your name, please:"))
    print("[Player 2]")
    player2 = str.lower(raw_input("Type in your name, please:"))


def randFirstPlayer():
    start = random.randint(1, 2)

    global FirstPlayer

    if (start == 1):
        FirstPlayer = player1
    else:
        FirstPlayer = player2


def flip_coin():
    coinOption = random.randint(1, 2)

    global coinSide

    if (coinOption == 1):
        coinSide = "heads"
    else:
        coinSide = "tails"


def getCoinOption():
    global player2Option
    global player1Option


    if (FirstPlayer == player1):
        print("")
        print str("[Player 1]:"), str.upper(player1)
        player1Option = str.lower(raw_input("Choose. Heads or tails?:"))

        if (player1Option == "heads"):
            player2Option = "tails"
        elif (player1Option == "tails"):
               player2Option = "heads"
        else:
            print ("Type in a valid option, please.")
            getCoinOption()
                
                
    else:
        print("")
        print str("[Player 2]:"), str.upper(player2)
        player2Option = str.lower(raw_input("Choose: heads or tails?: "))

        if (player2Option == "heads"):
            player1Option = "tails"
        elif (player2Option == "tails"):
            player1Option = "heads"
        else:
            print ("Type in a valid option, please.")
            getCoinOption()


def win():
    global winner

    if (player1Option == coinSide):
        winner = player1
    else:
        winner = player2

    print("")
    print str("You got"), str(coinSide)
    print str("The winner is:"), str.upper(winner)


create_players()
randFirstPlayer()
getCoinOption()
flip_coin()
win()
