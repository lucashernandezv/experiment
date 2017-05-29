import random

def createSystemHand():

    global sys_hand_num
    sys_hand_num = random.randint(1,3)
    global sys_hand_name

    if (sys_hand_num == 1):
        sys_hand_name = "Rock"
    elif (sys_hand_num == 2):
        sys_hand_name = "Paper"
    elif (sys_hand_num == 3):
        sys_hand_name = "Scissors"

def createPlayerHand():

    global player_choose_text
    global player_choose_num
    showmenu=True
    while showmenu:

        player_choose_text = str.lower(raw_input("Rock, Paper, Scissors: "))
        if (player_choose_text == "rock"):
            player_choose_num = 1
            showmenu = False
        elif (player_choose_text == "paper"):
            player_choose_num = 2
            showmenu = False
        elif (player_choose_text == "scissors"):
            player_choose_num = 3
            showmenu = False
        else:
            print("Please type in a valid option.")

def battle():
    if (sys_hand_num == 1):
        if (player_choose_num == 1):
            print ("Rock vs Rock")
        elif (player_choose_num==2):
            print str("Rock vs Paper. Player wins.")
        elif (player_choose_num==3):
            print ("Rock vs scissors. Computer wins")
    elif (sys_hand_num==2):
        if (player_choose_num == 1):
            print ("Paper vs Rock. Computer wins")
        elif (player_choose_num==2):
            print ("Draw")
        elif (player_choose_num==3):
            print str("Paper vs Scissors. Player wins.")
    elif (sys_hand_num==3):
        if (player_choose_num == 1):
            print str("Scissors vs Rock. Player wins.")
        elif (player_choose_num==2):
            print ("Scissors vs Paper. Computer wins")
        elif (player_choose_num==3):
            print ("Draw")

createSystemHand()
createPlayerHand()
battle()
