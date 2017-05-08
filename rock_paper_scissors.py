import random

class player():
  def __init__(self, name):
    self.name=name
    
# CREATES PLAYER 1
print("[Player 1]")
player1=player(input("Type in your name:"))

# DETERMINES COMPUTER MOVE
computerMove = random.randint(1,3)

if computerMove=="1":
  computerHand="Rock"
elif computerMove=="2":
  computerHand="Paper"
else:
  computerHand="Scissors"
  
# USER MOVE
def gameMenu():
  print("1. Rock")
  print("2. Paper")
  print("3. Scissors")
 
choose=True
while choose:
  gameMenu()

  choice=input("Type in your option: ")
  if choice == "1":
    userHand="Rock"
    print("Rock")
    choose=False
  elif choice == "2":
    userHand="Paper"
    print("Paper")
    choose=False
  elif choice == "3":
    userHand="Scissors"
    print("Scissors")
    choose=False
  else:
    print("Wrong option. Try again.")
    print("")

def battle():
  
  # COMPUTER ROCK VS USER ROCK
  if computerMove=="1" and choice=="1":
    print("Computer:",computerHand)
    print(player1.name,":",userHand)
    print(computerHand,"v/s",userHand,". Draw.")
  # COMPUTER ROCK VS USER PAPER
  elif computerMove=="1" and choice=="2":
    print("Computer:",computerHand)
    print(player1.name,":",userHand)
    print(userHand,"beats",computerHand)
  # COMPUTER ROCK VS USER SCISSORS
  elif computerMove=="1" and choice=="3":
    print("Computer:",computerHand)
    print(player1.name,":",userHand)
    print(computerHand,"beats",userHand)
  # COMPUTER PAPER VS USER ROCK
  elif computerMove=="2" and choice=="1":
    print("Computer:",computerHand)
    print(player1.name,":",userHand)
    print(computerHand,"beats",userHand)
  # COMPUTER PAPER VS USER PAPER
  elif computerMove=="2" and choice=="2":
    print("Computer:",computerHand)
    print(player1.name,":",userHand)
    print(computerHand,"v/s",userHand,". Draw.")
  # COMPUTER PAPER VS USER SCISSORS
  elif computerMove=="2" and choice=="3":
    print("Computer:",computerHand)
    print(player1.name,":",userHand)
    print(userHand,"beats",computerHand)
  # COMPUTER SCISSORS VS USER ROCK
  elif computerMove=="3" and choice=="1":
    print("Computer:",computerHand)
    print(player1.name,":",userHand)
    print(userHand,"beats",computerHand)
  # COMPUTER SCISSORS VS USER PAPER
  elif computerMove=="3" and choice=="2":
    print("Computer:",computerHand)
    print(player1.name,":",userHand)
    print(computerHand,"beats",userHand)
  # COMPUTER SCISSORS VS USER SCISSORS
  elif computerMove=="3" and choice=="3":
    print("Computer:",computerHand)
    print(player1.name,":",userHand)
    print(computerHand,"v/s",userHand,". Draw.")
