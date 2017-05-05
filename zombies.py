import random
class zombie:

    def __init__(self, zombieName, zombieHp, zombieEnergy, zombieDamage):
        self.zombieName = zombieName
        self.zombieHp = zombieHp
        self.zombieEnergy = zombieEnergy
        self.zombieDamage = zombieDamage


class player:

    def __init__(self, userHp):
        self.userHp = userHp


basic = zombie("basic", 450, 30, 50)
cone = zombie("cone", 450, 40, 40)
flag = zombie("flag", 450, 50, 30)

player = player(500)


def battle1():
    print("BATTLE1")
    zombieNumber = random.randint(1,100)
    userNumber = random.randint(1,100)

    if userNumber > zombieNumber:
        print("Player goes first")
        batlleCounter = 1

        # battle user vs basic

        player.userHp = player.userHp + basic.zombieEnergy
        basic.zombieHp = basic.zombieHp - basic.zombieDamage

        print("player HP: ",player.userHp)
        print(basic.zombieName, basic.zombieHp)

    else:
        print("Zombie goes first")
        player.userHp = player.userHp - basic.zombieEnergy
        basic.zombieHp = basic.zombieHp + basic.zombieEnergy

        print("player HP: ",player.userHp)
        print(basic.zombieName, basic.zombieHp)

def battle2():
    print("BATTLE2")
    zombieNumber = random.randint(1, 100)
    userNumber = random.randint(1, 100)

    if userNumber > zombieNumber:
        print("Player goes first")
        batlleCounter = 2

        # battle user vs basic

        player.userHp = player.userHp + cone.zombieEnergy
        cone.zombieHp = cone.zombieHp - cone.zombieDamage

        print("player HP: ",player.userHp)
        print(cone.zombieName, cone.zombieHp)

    else:

        print("Zombie goes first")
        player.userHp = player.userHp - cone.zombieEnergy
        cone.zombieHp = cone.zombieHp + cone.zombieEnergy

        print("player HP: ",player.userHp)
        print(cone.zombieName, cone.zombieHp)

def battle3():

    print("BATTLE3")
    zombieNumber = random.randint(1, 100)
    userNumber = random.randint(1, 100)

    if userNumber > zombieNumber:
        print("Player goes first")
        batlleCounter = 3

        # battle user vs flag

        player.userHp = player.userHp + flag.zombieEnergy
        flag.zombieHp = flag.zombieHp - flag.zombieDamage

        print("player HP: ",player.userHp)
        print(flag.zombieName, flag.zombieHp)

    else:
        print("Zombie goes first")
        player.userHp = player.userHp - flag.zombieEnergy
        flag.zombieHp = flag.zombieHp + flag.zombieEnergy

        print 'player HP: ',player.userHp
        print(flag.zombieName, cone.zombieHp)

battle1()
battle2()
battle3()

def winner():

    if player.userHp>flag.zombieHp:
        print("Player wins!")
    else:
        print("Zombie wins!")

winner()





