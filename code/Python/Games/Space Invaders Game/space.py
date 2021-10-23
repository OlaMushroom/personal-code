# Space Invader by Mahesh Sawant

import turtle
import winsound
import os
import math
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Space Invaders by Mahesh Sawant")
wn.bgpic("background.gif")

# Register the shape
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set the score to 0
score = 0

# Draw the pen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
#player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

# Choose a number of enemies
number_of_enemies = 10
# Creat an empty list of enemies
enemies = []

