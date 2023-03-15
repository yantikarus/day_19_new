from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet',
                            prompt='Which turtle color will win the race? (pink/ yellow/ red/ magenta / black or green')
turtle_names =['bob', 'jenny', 'wolly', 'nini', 'fluffy', 'milo']
color_list =['pink', 'yellow', 'red', 'magenta', 'black', 'green']
location_y = [-30, 0, 30, -60, 60, 90]
group_turtle = []


if user_bet:
    is_race_on = True

for i in range(0, 6):
    name = turtle_names[i]
    name = Turtle(shape='turtle')
    name.color(color_list[i])
    name.penup()
    name.goto(x=-230, y=location_y[i])
    group_turtle.append(name)

while is_race_on:
    for i in group_turtle:
        if i.xcor() > 220:
            winning_color = i.pencolor()
            is_race_on = False
            if user_bet == winning_color:
                print(f'You won! The winner is the {winning_color} turtle')
            else:
                print(f'You lost! The winner is the {winning_color} turtle')
        rand_speed = random.randint(0, 10)
        i.forward(rand_speed)





# def move_forward():
#     tim.forward(50)
#
#
# def move_backwards():
#     tim.back(50)
#
#
# def turn_left():
#     tim.left(10)
#
#
# def turn_right():
#     tim.right(10)
#
#
# def clear_drawing():
#     tim.penup()
#     tim.home()
#     tim.clear()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(move_forward, 'w')
# screen.onkey(move_backwards, 's')
# screen.onkey(turn_left, 'a')
# screen.onkey(turn_right, 'd')
# screen.onkey(clear_drawing, 'c')


screen.exitonclick()
