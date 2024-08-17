from turtle import Turtle,Screen
import random

turtle1 = Turtle()
turtle2 = Turtle()
turtle3 = Turtle()
turtle4 = Turtle()
turtle5 = Turtle()
turtle6  = Turtle()
turtle7 = Turtle()

main_turtle = Turtle()
main_turtle.ht()
main_turtle.penup()
main_turtle.setpos(490,-190)
main_turtle.pendown()
main_turtle.goto(490,190)


list_of_turtle = [turtle1,turtle2,turtle3,turtle4,turtle5,turtle6,turtle7]
turtle_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
random.shuffle(turtle_colors)


screen = Screen()
screen.setup(1000,400)

def turtle_position(turtle, postion_x, position_y):
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(postion_x,position_y)

position = 150
adding_color_to_turtle = 0

for setting_turtle_position in list_of_turtle:
    setting_turtle_position.color(turtle_colors[adding_color_to_turtle])
    turtle_position(turtle=setting_turtle_position,postion_x=-400,position_y=position)
    adding_color_to_turtle += 1
    position -= 50

user_bet = screen.textinput("Choose the Winner", f"Choose the winner form the list {turtle_colors} ?").lower()

turtle_keep_moving = True
while turtle_keep_moving:
    for moving_turtle in list_of_turtle:
        moving_turtle.forward(random.randint(5,20))
        winner = moving_turtle.xcor()
        if winner >= 490:
            which_turtle_wins = list_of_turtle.index(moving_turtle)
            turtle_color_wins = turtle_colors[which_turtle_wins]
            if user_bet == turtle_color_wins:
                print("You Wins")
                turtle_keep_moving = False
            else:
                print("You loose")
                print(f"The winner is {turtle_color_winsa}")
                turtle_keep_moving = False




    
screen.exitonclick()