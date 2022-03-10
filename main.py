import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
choice = screen.textinput("Turtle Bet", "Choose the color of the turtle you think will win.")
turtle_colors = ["red", "blue", "yellow", "green", "purple", "pink"]
turtles = []
position = [0, 30, 60, -30, -60, -90]
i = 0
for i in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[i])
    new_turtle.goto(-230,  position[i])
    turtles.append(new_turtle)
    i += 1


start_race = False
if choice:
    start_race = True
while start_race:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 220:
            start_race = False
            winner = turtle.pencolor()

if choice == winner:
    print(f"You won! The winner is {winner}")
else:
    print(f"You lost. The winner is {winner}")




screen.exitonclick()
