import turtle
bob = turtle.Turtle()

bob.color(0,0,0)

#circle with color----------------------------------
def circle(radius,border_color,fill_color):
        bob.color(border_color)
        bob.fillcolor(fill_color)
        bob.begin_fill()
        bob.circle(radius)
        bob.end_fill()

#design with different colored lines-----------------
def polygon(sides,dist):
    angle=360/sides
    for times in range(90):
        for times in range(50):
            bob.color(0,0,255)
            bob.forward(times)
            bob.left(angle)
            bob.color(0,255,255)
            bob.forward(times +20)
            bob.left(angle)
            bob.color(255,0,255)
            bob.forward(times +30)
            bob.left(angle)
        jump(0,0)
        bob.left(5)
        
#jump to a new location------------------------------
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
