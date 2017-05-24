`import random

name = str.upper(raw_input("Please enter your name:"))

##def history(): commented out because it does nothing yet
    ##global userattk
    ##userattk = newShipX,newShipY
    ##print userattk

def printmap(): ## MAP SIZE 5x5
    i = 0
    j = 0
    print ("  A B C D E") ## X AXIS
 
    while (i<5):
        j = j + 1
        print j,("0 0 0 0 0") ## Y AXIS
        i = i + 1
        
def computerCreateShip(): ## DETERMINES COMPUTER'S SHIP LOCATION
    
    global compYShip
    compYShip = random.randint(1,5)
    global compX
    compX = random.randint(1,5)
    
    global compXShip
    
    if compX == 1:
        compXShip = "a"
    elif compX == 2:
        compXShip = "b"
    elif compX == 3:
        compXShip = "c"
    elif compX == 4:
        compXShip = "d"
    elif compX == 5:
        compXShip = "e"
    
    ## print ("[COMPUTER SHIP:"),compXShip,compYShip,("]") ##ERASE COMMENT TO PRINT COMPUTER'S SHIP COORDINATES

def win(): ## PRINT OUT THE TRIES COUNTER
    print("You win!")
    if (attackCounter == 1):
        print ("Congratulations,"),str(name),("!")
        print("You got it right in the first try!")
    else:
        print("Congratulations,"),str(name),("!")
        print("You got it in"),int(attackCounter),("tries.")

def attackShip():
    
    ## ADD MORE ITEMS IN THE DICTIONARIES TO INCREASE MAP SIZE
    global xvalues 
    xvalues = ["a", "b", "c","d", "e"]
    global yvalues
    yvalues = ["1", "2", "3", "4", "5"]
    
    global attackCounter
    attackCounter = 0
    
    ## GETS USER INPUT AND COMPARES IT TO COMPUTER'S SHIP LOCATION. REPEATS UNTIL WIN.
    attack = True
    while attack:
        showx = True
        global newShipX
        while showx:
            newShipX = str.lower(raw_input("Type in the X-Axis coordinate: "))
            if (newShipX in xvalues):
                showx=False ## VALIDATES DATA INPUT
            if not (newShipX in xvalues):
                print("[WRONG X VALUE]")
    
        showy = True
        global newShipY
        while showy:
            newShipY = str.lower(raw_input("Type in the Y-Axis coordinate: "))
            if (newShipY in yvalues):
                showy=False ## VALIDATES DATA INPUT
            else:
                print("[WRONG Y VALUE]")
            
        attackCounter = attackCounter + 1 ## INCREASES COUNTER
        
        if (str(newShipY) == str(compYShip)) and (str(newShipX) == str(compXShip)):
            print ("DESTROYED")
            attack = False
            win()
        elif (str(newShipY) == str(compYShip)):
            print ("HIT! (Y-Axis)") ## DISPLAYS HIT HINT
        elif (str(newShipX) == str(compXShip)):
            print("HIT! (X-Axis)") ## DISPLAYS HIT HINT
        else:
            print ("The attack had no effect.")
            
## CALLS FUNCTIONS 
printmap()
computerCreateShip()
attackShip()
