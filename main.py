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


def rechteck(laenge, hoehe, abstand, x, y):
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.pendown()

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


    if laenge > 3 * abstand and hoehe > 2 * abstand:
        if abstand * 3 < laenge - 6 * abstand:
            laenge1 = randint(abstand * 3,laenge - 6 * abstand)

            hoehe1 = hoehe - 2 * abstand

            myTurtlePos = myTurtle.pos()
            x1 = myTurtlePos[0]
            y2 = myTurtlePos[1]
            rechteck(laenge1,hoehe1,abstand,myTurtlePos[0],myTurtlePos[1])




            myTurtle.penup()
            myTurtle.forward(laenge1 + abstand)
            myTurtle.pendown()

            myTurtlePos = myTurtle.pos()

            rechteck(laenge - (laenge1 + 3 * abstand), hoehe1, abstand, myTurtlePos[0], myTurtlePos[1])#



            myTurtle.penup()
            myTurtle.goto(x1, y2)
            rechteck_schoner(laenge1, hoehe1, abstand, x1, y2)


            myTurtle.penup()
            myTurtle.goto(x,y)
            myTurtle.forward(laenge + abstand)

















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
aussen_rechteck(450,450,10,0,0)

