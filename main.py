from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def forward():
    turtle.forward(30)
def backward():
    turtle.forward(-30)
def right():
    turtle.left(20)
def left():
    turtle.right(20)
screen.onkey(fun=forward, key="Up")
screen.onkey(fun=backward, key="Down")
screen.onkey(fun=right, key="Right")
screen.onkey(fun=left, key="Left")



screen.listen()


screen.exitonclick()