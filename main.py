from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(50)


def move_backwards():
    tim.back(50)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear_drawing():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear_drawing, 'c')


screen.exitonclick()
