import turtle
import random

maTortue = turtle.Turtle()
maTortue.penup()
maTortue.setpos(0, -400)
maTortue.pendown()
turtle.delay(0)
maTortue.speed(0)
"""
#Exercice 1:

def carre():
    maTortue.speed(1)
    for i in range(4):
        maTortue.forward(100)
        maTortue.left(90)

#carre()

def cercle():
    maTortue.speed(1)
    maTortue.circle(200, None, 300)

#cercle()

#Exercice 2 :

def escargotCarre():
    maTortue.speed(10)
    size = 400
    while size > 0:
        maTortue.forward(size)
        maTortue.left(90)
        size -=3

#escargotCarre()

def escargotRond():
    maTortue.speed(100)
    size = 400
    while size > 0:
        maTortue.circle(size, 90)
        size-=3

#escargotRond()
"""
#Exercice 3 :

Tortue1 = turtle.Turtle()
Tortue2 = turtle.Turtle()
Tortue3 = turtle.Turtle()
Tortue4 = turtle.Turtle()

def pas(maTortue):
    randomDir = random.randint(0,2)
    if randomDir == 0:
        maTortue.left(90)
    elif randomDir == 1:
        maTortue.right(90)
    maTortue.forward(10)


def marcheMulti(Tortue1, Tortue2, Tortue3, Tortue4):
    Tortue1.color(randomColor())
    Tortue2.color(randomColor())
    Tortue3.color(randomColor())
    Tortue4.color(randomColor())
    while True:
        pas(Tortue1)
        pas(Tortue2)
        pas(Tortue3)
        pas(Tortue4)


def randomColor():
    color = '#'
    letters = "0123456789ABCDEF"
    for i in range (6):
        rand = random.randint(0,15)
        color += letters[rand]
    return color


"""def marche(maTortue):
    maTortue.penup()
    maTortue.setpos(0,0)
    maTortue.pendown()
    while True:
        randomDir = random.randint(0,2)
        if randomDir == 0:
            maTortue.left(90)
        elif randomDir == 1:
            maTortue.right(90)
        maTortue.forward(10)


marche()"""

marcheMulti(Tortue1, Tortue2, Tortue3, Tortue4)

input()