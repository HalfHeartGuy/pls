import random
import turtle
from turtle import *
from random import randint

screen = turtle.getscreen()
screen.clear()
screen.title("Game")
screen.colormode(255)
myTurtle = turtle.Turtle()
myTurtle.reset()


def colors():
    colors = []
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colors.append(r)
    colors.append(g)
    colors.append(b)
    return colors



def rechteck(laenge, hoehe, x, y):

    
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.pendown()
    color = colors()
    myTurtle.color((color[0],color[1],color[2]))
    for i in range(0, 2):
        myTurtle.forward(laenge)
        myTurtle.right(90)
        myTurtle.forward(hoehe)
        myTurtle.right(90)



def positionieren(abstand):


    myTurtle.penup()
    myTurtle.forward(abstand)
    myTurtle.right(90)
    myTurtle.forward(abstand)
    myTurtle.left(90)




def rechteck_schoner(laenge, hoehe, abstand, x, y):
    positionieren(abstand)

    candrawBox = candraw2boxes(laenge,hoehe,abstand)

    if candrawBox:
        if abstand * 3 < laenge:
            laenge1 = randint(abstand * 3,laenge)

            hoehe1 = hoehe - 2 * abstand

            myTurtlePos = myTurtle.pos()
            x1 = myTurtlePos[0]
            y2 = myTurtlePos[1]
            rechteck(laenge1,hoehe1,myTurtlePos[0],myTurtlePos[1])




            myTurtle.penup()
            myTurtle.forward(laenge1 + abstand)
            myTurtle.pendown()

            myTurtlePos = myTurtle.pos()


            rechteck(laenge - (laenge1 + 3 * abstand), hoehe1,  myTurtlePos[0], myTurtlePos[1])#
            rechteck_schoner(laenge - (laenge1 + 3 * abstand), hoehe1, abstand, myTurtlePos[0], myTurtlePos[1])


            myTurtle.penup()
            myTurtle.goto(x1, y2)
            rechteck_schoner(laenge1, hoehe1, abstand, x1, y2)


            myTurtle.penup()
            myTurtle.goto(x,y)
            myTurtle.forward(laenge + abstand)





def candraw2boxes(laenge, hoehe, abstand):
    if laenge > 3 * abstand and hoehe > 2 * abstand:
        return True              
    
    elif laenge > 2 * abstand and hoehe > 3 * abstand:
        return True
    
    
    else:
        False














def aussen_rechteck(laenge,hoehe,abstand,startX,startY):
    myTurtle.penup()
    myTurtle.goto(startX,startY)
    myTurtle.pendown()

    for i in range(0,2):
        myTurtle.forward(laenge)
        myTurtle.right(90)
        myTurtle.forward(hoehe)
        myTurtle.right(90)
    if laenge > 3 * abstand and hoehe > 2 * abstand:

        rechteck_schoner(laenge,hoehe,abstand,startX,startY)
aussen_rechteck(250,350,10,-200,200)

