import turtle
import time
import threading

class setup:
    def __init__(self,turtle_name,file_name):
        turtle_name.hideturtle()
        turtle.addshape(file_name)
        turtle_name.shape(file_name)
        turtle_name.penup()
            
        
def build():
    setup(blinky,"blinky_left.gif")
    setup(lnky,"lnky_left.gif")
    setup(logo,"logo.gif")
    setup(pac_man,"pac_man_left.gif")

    turtle.addshape("pac_man_right.gif")
    turtle.addshape("pac_man_up.gif")
    turtle.addshape("pac_man_down.gif")
    turtle.addshape("lnky_right.gif")
    turtle.addshape("blinky_right.gif")
    
    logo.speed(0)
    logo.goto(0,6)
    logo.showturtle()

#make map
def make_map():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(5,5)
    turtle.pendown()
    turtle.goto(5,-5)
    turtle.goto(-5,-5)
    turtle.goto(-5,5)
    turtle.goto(5,5)
    turtle.penup()
    turtle.goto(0,5)
    turtle.pendown()
    turtle.goto(0,3)
    turtle.goto(-1,3)
    turtle.goto(0,3)
    turtle.goto(0,1)
    turtle.penup()
    turtle.goto(0,-1)
    turtle.pendown()
    turtle.goto(0,-1)
    turtle.goto(0,-2)
    turtle.goto(0,-1)
    turtle.goto(0,-1)
    turtle.penup()
    turtle.goto(0,-2)
    turtle.pendown()
    turtle.goto(-3,-2)
    turtle.goto(-3,-1)
    turtle.penup()
    turtle.goto(0,-2)
    turtle.pendown()
    turtle.goto(0,-3)
    turtle.goto(3,-3)
    turtle.goto(0,-3)
    turtle.goto(0,-5)
    turtle.penup()
    turtle.goto(3,3)
    turtle.pendown()
    turtle.goto(3,1)
    turtle.goto(2,1)
    turtle.goto(2,-1)
    turtle.penup()
    turtle.goto(-3,3)
    turtle.pendown()
    turtle.goto(-3,1)
    turtle.penup()
    
def up():
    pac_man.shape("pac_man_up.gif")
    pac_man.goto(pac_man.xcor(),pac_man.ycor()+1)
    c()

def down():
    pac_man.shape("pac_man_down.gif")
    pac_man.goto(pac_man.xcor(),pac_man.ycor()-1)
    c()


def left():
    pac_man.shape("pac_man_left.gif")
    pac_man.goto(pac_man.xcor()-1,pac_man.ycor())
    c()

def right():
    pac_man.shape("pac_man_right.gif")
    pac_man.goto(pac_man.xcor()+1,pac_man.ycor())
    c()

def c():
    if ball.position() == pac_man.position():
        ball.hideturtle( )
        print("you win")

def blinky_mv():
    blinky.goto(4,4)
    blinky.showturtle()
    win = True
    while win == True and ball.isvisible():
        time.sleep(1)
        if pac_man.xcor() >= -1 and pac_man.ycor() > 0:
            if pac_man.xcor() < blinky.xcor():
                blinky.goto(blinky.xcor()-1,blinky.ycor())
            elif pac_man.ycor() < blinky.ycor():
                blinky.goto(blinky.xcor(),blinky.ycor()-1)

        elif pac_man.xcor() > 0 and pac_man.ycor() < 0:
            if pac_man.xcor() < blinky.xcor():
                blinky.goto(blinky.xcor()-1,blinky.ycor())
            elif pac_man.ycor() < blinky.ycor():
                blinky.goto(blinky.xcor(),blinky.ycor()+1)

        if blinky.position() == pac_man.position():
            pac_man.hideturtle( )
            win = False

turtle.setworldcoordinates(-6, -6, 6, 6)

blinky = turtle.Turtle()
lnky = turtle.Turtle()
logo = turtle.Turtle()
pac_man = turtle.Turtle()
ball = turtle.Turtle()

build()
#turtle.getshapes() 
make_map()
pac_man.showturtle()

x=0
y=0

ball.shapesize(1,1,1)
ball.shape("circle")
ball.penup()
ball.goto(2,2)

turtle.listen()
turtle.onkeypress(up, "Up")  
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

t = threading.Thread(target=blinky_mv, args=())
t.start()

turtle.done()
