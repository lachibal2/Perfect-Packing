#perfect packing program
#by: Lachi Balabanski
import math
from turtle import *
def getRadius(boxLen, numCircles):
    return boxLen / (2 * math.sqrt(numCircles))
def drawCircle(turtle, radius, center):
    """
    turtle is an instance of Turtle
    radius is int of circle radius
    center is a tuple of the coords of the circle center
    draws a circle with center at center and radius of radius
    """
    turtle.penup()
    turtle.goto(center)
    turtle.pendown()
    turtle.circle(radius)
def drawBox(turtle,center=(0,0),side=500):
    """
    turtle is an instance of Turtle
    side is an int of the length of one side
    center is a tuple of the center of the square
    draws a square with a center at center and side length of square
    """
    turtle.penup()
    turtle.goto(center)
    turtle.forward(side/2)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(side/2)
    for i in range(3):
        turtle.left(90)
        turtle.forward(side)
    turtle.left(90)
    turtle.forward(side/2)
def makeCircles(turtle,numCircles,boxCorner,boxLen=500):
    """
    turtle is an instance of Turtle
    numCircles is an int of the number of circles
    boxCorner is a tuple of the coordinates of the top left corner of the box
    boxLen is an int of the length of the box
    draws numCircles circles inside the box
    efficency: O(n^2)
    """
    rad = getRadius(boxLen,numCircles)
    currentPos = boxCorner
    turtle.penup()
    turtle.goto(boxCorner)
    turtle.pendown()
    for i in range(int(math.sqrt(numCircles))):
        for j in range(int(math.sqrt(numCircles))):
            currentPos = (currentPos[0] + (2 * rad), currentPos[1] - rad)
            drawCircle(turtle, rad, currentPos)
            currentPos= (currentPos[0], currentPos[1] + rad)
        currentPos = (boxCorner[0], currentPos[1] - (2 * rad))
def userInput():
    while True:
        try:
            user = input('Number of circles, must be a perfect square: ')
            sqrtUser = math.sqrt(int(user))
            if str(sqrtUser)[-1:] == '0' and len(str(sqrtUser).split('.')[1]) == 1:
                break
            else:
                print("Not a perfect square, try again")
        except ValueError:
            print("Please type a number")
    return int(user)
def circleArea(numCircles,radius,boxLen=500):
    return(str((radius ** 2) * numCircles) + 'π units^2')
boxLen = 500
numCircles = userInput()
t = Turtle()
t.speed(0) #sets turtle to max speed
space = Screen()
drawBox(t)
makeCircles(t,numCircles,(-250,250))
print("Side length of box: " + str(boxLen))
print("Number of Circles: " + str(numCircles))
print("------------------")
print("Area of all of the circles: " + str(circleArea(numCircles,getRadius(boxLen,numCircles))))