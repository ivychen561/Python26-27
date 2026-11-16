from myFunctions import *
from random import *

turtle.colormode(255)

turtle.bgcolor("black")
turtle.tracer(0)
bob.width(1)

#design-------------------------------------
polygon(50,100)

jump(0,0)
bob.setheading(0)

#top row of circles-------------------------
border="white"
jump(-450,350)
for times in range(16):
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    fill=(r,0,b)
    circle(30,border,fill)
    bob.penup()
    bob.forward(60)
    bob.pendown()
    
#bottom row of circles----------------------
jump(-450,-400)
for times in range(16):
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    fill=(r,0,b)
    circle(30,border,fill)
    bob.penup()
    bob.forward(60)
    bob.pendown()
    
    

