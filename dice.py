
import random

class dice:
  def __init__(self, side1, side2, side3, side4, side5, side6):
    self.side1=side1
    self.side2=side2
    self.side3=side3
    self.side4=side4
    self.side5=side5
    self.side6=side6
    
dice1=dice(1, 2, 3, 4, 5, 6)

keepRolling=True
counter = 0

def rollDice():
  displaySide=random.randint(1,6)
  
  if displaySide == 1:
    print("You got a: ",dice1.side1)
  elif displaySide == 2:
    print("You got a: ",dice1.side2)
  elif displaySide == 3:
    print("You got a: ",dice1.side3)
  elif displaySide == 4:
    print("You got a: ",dice1.side4)
  elif displaySide == 5:
    print("You got a: ",dice1.side5)
  elif displaySide == 6:
    print("You got a: ",dice1.side6)
    
def stop():
  print("You rolled the dice ",counter," times.")
  
while keepRolling:
  
  choice = input("Press ENTER to roll the dice or q to quit: ")
  print("")
  
  if choice == "q":
    stop()
    keepRolling=False
  else:
    rollDice()
    counter = counter+1