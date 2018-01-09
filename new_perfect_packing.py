from tkinter import *
import math
import time
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
def userInput(string, label):
    try:
        sqrtUser = math.sqrt(int(string))
        if str(sqrtUser)[-1:] == '0' and len(str(sqrtUser).split('.')[1]) == 1:
            return True
        else:
            label.configure(text='Not a perfect Square', fg='red')
            return False
    except ValueError:
        label.configure(text='Invalid Input', fg='red')
        return False
    return False
def circleArea(numCircles,radius,boxLen=500):
    return(str(round((radius ** 2) * numCircles,2)) + 'π units^2')
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.startWind()
    def startWind(self):
        self.pack(fill=BOTH, expand=1)
        exitButton = Button(self, height=2, width=20, bg='red', text='Exit To Desktop',command=lambda:quit())
        exitButton.place(x=0,y=0)
        lb = Label(self.master, text='Number of Circles:', fg='black')
        lb.place(x=190,y=0)
        space = Canvas(self.master, width=600, height=600)
        space.pack()
        submit = Button(text='Create Circles', bg='white', bd=5, command=lambda:self.submitEntries(user, output, space, submit))
        submit.place(x=450,y=0)
        user = Entry(self.master)
        user.place(x=300,y=0)
        output = Label(self.master, text=' ', width=1, height=3,bg='white')
        output.pack(side=BOTTOM, expand=1, fill=BOTH)
    def submitEntries(self,entry,label,space,button):
        button.configure(state=DISABLED)
        boxLen = 500
        numCircles = userInput(entry.get(),label)
        if numCircles == True:
            numCircles = int(entry.get())
        else:
            label.configure(text='Not perfect square', fg='red')
            button.configure(state=NORMAL)
            return None
        label.configure(text='Drawing...', fg='black')
        space.delete('all')
        start = time.time()
        t = RawTurtle(space)
        t.speed(0) #sets turtle to max speed
        label.configure(drawBox(t,(0,0),boxLen))
        makeCircles(t,numCircles,(-1 * (boxLen/2), (boxLen/2)),boxLen)
        elapsed = round((time.time() - start),2)
        label.configure(text="""        Done in  + """ + str(elapsed) +  """ seconds!
        Side length of box: """ + str(boxLen) + """
        Number of Circles:  """+ str(numCircles) + """
        ------------------
        Area of all of the circles: """ + str(circleArea(numCircles,getRadius(boxLen,numCircles))))
        button.configure(state=NORMAL)
root = Tk()
root.geometry('1000x750')
win = Window(root)
root.mainloop()
