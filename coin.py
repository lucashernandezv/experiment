import random


class coin:
    def __init__(self, heads, tails):
        self.heads = heads
        self.tails = tails


coin1 = coin("Heads", "Tails")

flip = True
flipCounter = 0


# headsCounter = 0
# tailsCounter = 0

def rollDice():
    side = random.randint(1, 2)

    if side == 1:
        print("You got", coin1.heads)
        # headsCounter=headsCounter+1
    else:
        print("You got", coin1.tails)
        # tailsCounter=tailsCounter+1


def stop():
    print("You flipped", flipCounter, "coins.")
    # print("You got",headsCounter,"heads and",tailsCounter,"tails.")


while flip:
    choice = raw_input("Press ENTER to flip a coin, or press q to exit: ")
    print("")

    if choice == "q":
        stop()
        flip = False

    else:
        rollDice()
        flipCounter = flipCounter + 1

