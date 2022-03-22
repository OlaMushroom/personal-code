import turtle
import time
import random

delay = 0.1

# diem
score=0
high_score=0

# thiet lap mang hinh
wn=turtle.Screen()
wn.title(".")
wn.bgcolor("green")
wn.setup(width=600, height=600)


# dau ran
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

# thuc an cho ran
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments=[]

# ghi diem va diem cao nhat
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions: chuc nang
#dinh nghia cac ham di chuyen
def go_up():
    if head.direction != "down":
        head.direction="up"

def go_down():
    if head.direction != "up":
        head.direction="down"

def go_left():
    if head.direction != "right":
        head.direction="left"

def go_right():
    if head.direction != "left":
        head.direction="right"

def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)

# khi bam phim thi di chuyen
wn.listen()
#up-->nut w
wn.onkeypress(go_up,"w")
#down-->nut s
wn.onkeypress(go_down,"s")
#left-->nut a
wn.onkeypress(go_left,"a")
#right-->nut d
wn.onkeypress(go_right,"d")

# vong lap cho game
while True:
    

