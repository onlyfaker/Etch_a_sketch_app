from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def forward():
    turtle.forward(30)
def backward():
    turtle.forward(-30)
def right():
    turtle.right(20)
def left():
    turtle.left(20)
def clear_the_screen():
    turtle.clear()
    turtle.penup()
    turtle.ht()
    turtle.speed(0)
    turtle.goto(0,0)
    turtle.pendown()
    turtle.st()
    turtle.speed('slow')

screen.onkey( key="w",fun=forward)
screen.onkey(fun=backward, key="s")
screen.onkey(fun=right, key="d")
screen.onkey(fun=left, key="a")
screen.onkey(fun=clear_the_screen, key="c")



screen.listen()
screen.exitonclick()