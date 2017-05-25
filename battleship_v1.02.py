import random

name = str.upper(raw_input("Please enter your name:"))

##def history(): commented out because it does nothing yet
    ##global userattk
    ##userattk = newShipX,newShipY
    ##print userattk

def printmap(): ## CREATES AND DISPLAYS MAP
    i = 0
    j = 0
    print("(x-axis: horizontal)")
    print("(y-axis: vertical)")
    print("")
    print ("  A B C D E") ## X-AXIS
 
    while (i<5): ##SETS THE MAP SIZE TO 5X5
        j = j + 1 ## Y-AXIS NUMBERS
        print j,("0 0 0 0 0") ## Y-AXIS
        i = i + 1 ## X-AXIS LETTERS
        
def computerCreateShip():
    
    global compYShip
    compYShip = random.randint(1,5) ## ALLOCATES COMPUTER'S SHIP Y-AXIS. CHANGE RANDOM LIMITS WHEN  INCREASING MAP SIZE
    global compX
    compX = random.randint(1,5)## ALLOCATES COMPUTER'S SHIP X-AXIS. CHANGE RANDOM LIMITS WHEN INCREASING MAP SIZE
    
    global compXShip
    
    ## TRANSLATES X-AXIS NUMBER TO A LETTER. ADD FURTHER IFS WHEN INCREASING MAP SIZE
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
    print("")
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
            print("")
            ## USER INPUT X-AXIS GUESS 
            newShipX = str.lower(raw_input("Type in the X-Axis coordinate: "))
            if (newShipX in xvalues):
                showx=False ## VALIDATES DATA INPUT
            if not (newShipX in xvalues):
                print("[WRONG X VALUE]")
    
        showy = True
        global newShipY
        while showy:
            # USER INPUT Y-AXIS GUESS 
            newShipY = str.lower(raw_input("Type in the Y-Axis coordinate: "))
            print("")
            if (newShipY in yvalues):
                showy=False ## VALIDATES DATA INPUT
            else:
                print("[WRONG Y VALUE]")
            
        attackCounter = attackCounter + 1 ## INCREASES COUNTER
        
        battle()
        
def battle(): ## SEPARATED THIS INTO AN INDEPENDENT FUNCTION, TO BE ABLE TO CALL IT FROM OUTSIDE
           
        ## IF USER GUESS MATCHES COMPUTER'S SHIP LOCATION, THE SHIP IS DESTROYED 
        if (str(newShipY) == str(compYShip)) and (str(newShipX) == str(compXShip)):
            print ("----- DESTROYED ENEMY'S SHIP!! -----")
            attack = False
            win()
            
        elif (str(newShipY) == str(compYShip)):
             ## PRINTS LOCATION WHERE ATTACK LANDED 
            print str("[ATTACK LANDED ON:"), str.upper(newShipX),str(newShipY),str("]") 
            print ("HIT ON Y-AXIS") ## DISPLAYS HIT HINT
        elif (str(newShipX) == str(compXShip)):
            ## PRINTS LOCATION WHERE ATTACK LANDED 
            print str("[ATTACK LANDED ON:"), str.upper(newShipX),str(newShipY),str("]")
            print("HIT ON X-AXIS") ## DISPLAYS HIT HINT
        else:
            ## PRINTS LOCATION WHERE ATTACK LANDED 
            print str("[ATTACK LANDED ON:"), str.upper(newShipX),str(newShipY),str("]")
            print ("The attack had no effect.")
            
## CALL FUNCTIONS 
printmap()
computerCreateShip()
attackShip()

