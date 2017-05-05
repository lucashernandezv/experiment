import random
import math




class square:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class triangle:
    def __init__(self, base, height, side):
        self.base = base
        self.height = height
        self.side = side

class circle:
    def __init__(self, radius):
        self.radius = radius

def calCirArea():
    circle1=circle(input("Enter the circle radius: "))

    circleArea=math.pi*circle1.radius
    print(circleArea)

def calCirPerimeter():
    circle1=circle(input("Enter the circle radius: "))

    circlePerimeter=2*(math.pi*circle1.radius)
    print(circlePerimeter)


def calSqArea():
    square1=square(input("Enter the square length: "), input("Enter the square width: "))

    squareArea = square1.length*square1.width
    print(squareArea)

def calSqPerimeter():
    square1=square(input("Enter the square length: "), random.randint(1,100))

    squarePerimeter = square1.length*4
    print(squarePerimeter)

def calTrArea():
    triangle1 = triangle(input("Enter the base of the triangle: "), input("Enter the height of the triangle: "), input("Enter the side of the triangle:"))

    triangleArea = (triangle1.base*triangle1.height)/2
    print(triangleArea)

def calTrPerimeter():
    triangle1 = triangle(random.randint(1,100), random.randint(1,100), input("Enter the side of the triangle: "))

    trianglePerimeter = triangle1.side*3
    print(trianglePerimeter)


def displayMenu():

    print("1- Calculate the area of a square.")
    print("2- Calculate the perimeter of a square.")
    print("3- Calculate the area of a triangle.")
    print("4- Calculate the perimeter of a triangle.")
    print("5- Calculate the area of a circle.")
    print("6- Calculate the perimeter of a circle")
    print("7- Exit.")

loop = True

while loop:
    displayMenu()
    choice = input("Enter your choice here: ")

    if choice==1:
        calSqArea()
    elif choice==2:
        calSqPerimeter()
    elif choice==3:
        calTrArea()
    elif choice==4:
        calTrPerimeter()
    elif choice==5:
        calCirArea()
    elif choice==6:
        calCirPerimeter()
    elif choice==7:
        loop = False

    else:
        raw_input("Wrong option. Please try again.")





