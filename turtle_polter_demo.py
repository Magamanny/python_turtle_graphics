import turtle
from random import random
def patternA():
    t = turtle.Turtle()
    for steps in range(100):
        for c in ('blue','red','green'):
            t.color(c)
            t.forward(steps)
            t.right(30)
def patternB():
    colors = ['red','dark red']
    t = turtle.Turtle()
    for number in range(200):
        t.forward(2*number)
        t.right(89)
        t.pencolor(colors[number%2])
def patternC():
    t = turtle.Turtle()
    t.color('red')
    t.fillcolor('yellow')
    t.begin_fill()
    for steps in range(100):
        t.forward(300)
        t.left(170)
        # check if it return to the origin
        if abs(t.pos())<0.00001:
            break
    t.end_fill()
def patternX():
    alpha=1.0004
    t = turtle.Turtle()
    for steps in range(10*360):
        t.right(1.00000*alpha*steps)
        t.fd(6)
    print(t.pos())
def patternY():
    rule = {
    'x':['y','+','x','+','y'],
    'y':['x','-','y','-','x'],
    '+':['+'],
    '-':['-']
    }
    system = [['x']]
    n=8
    for i in range(n):
        t = []
        for s in system[-1]:
            for r in rule[s]:
                t.append(r)
        #print(t)
        system.append(t)
    print(system[1])
    t = turtle.Turtle()
    t.penup()
    t.right(90)
    t.fd(200)
    t.right(90)
    t.fd(200)
    t.right(180)
    t.pendown()
    for i in system[n]:
        if(i=='x' or i=='y'):
            t.fd(2)
        elif(i=='+'):
            t.right(60)
        elif(i=='-'):
            t.left(60)
turtle.bgcolor('white')
turtle.tracer(0, 0)
#patternA()
patternB()
#patternC()
#patternX()
#patternY()
turtle.done()