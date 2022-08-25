import turtle

class addshape: 
    def __init__(role,y,x):
        y = turtle.Turtle()
        role = turtle.Screen()
        role.addshape(x)
        y.shape(x)
        y.penup()
        y.hideturtle( )
        
def build():
    blinky_left = turtle.Turtle()
    addshape(blinky_left,'blinky_left.gif')

    blinky_right = turtle.Turtle()
    addshape(blinky_right,'blinky_right.gif')

    lnky_left = turtle.Turtle()
    addshape(lnky_left,'lnky_left.gif')

    lnky_right = turtle.Turtle()
    addshape(lnky_right,'lnky_right.gif')

    logo = turtle.Turtle()
    addshape(logo,'logo.gif')
 
turtle.setworldcoordinates(-100, -100, 100, 100)
build()
turtle.addshape("dog_s.gif")
turtle.shape("dog_s.gif")
turtle.done()
