from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def turn_left():
    tim.left(90)

def turn_right():
    tim.right(90)

screen.listen()
screen.onkey(move_forward,"space")
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")
screen.exitonclick()
