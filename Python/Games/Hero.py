import math, random
from turtle import *
s = Screen()
s.setup(700, 700)
s.bgcolor('#000')
s.title('Hể ồ')

class Hero(Turtle):
  def __init__(self):
    Turtle.__init__(self)
    self.penup()
    self.speed(0)
    self.shape('square')
    self.color('#FFF')
    self.speed = 5
  
  def move(self):
    self.forward(self.speed)
    if self.xcor() > 300:
      self.setx(-300)
    
    if self.xcor() < -300:
      self.setx(300)
    
    if self.ycor() > 300:
      self.sety(-300)
    
    if self.ycor() < -300:
      self.sety(300)
  
  def l(self):
    while self.heading() != 180:
      self.setheading(180)
  
  def r(self):
    if self.heading() != 0:
      self.setheading(0)

  def u(self):
    if self.heading() != 90:
      self.setheading(90)

  def d(self):
    if self.heading() != 270:
      self.setheading(270)
    
  def spin(self):
    if True:
      self.right(10)
  
  def accel(self):
    self.speed += 1
  
  def decel(self):
    self.speed -= 1
  
class Monster(Turtle):
  def __init__(self):
    Turtle.__init__(self)
    self.penup()
    self.speed(0)
    self.shape('turtle')
    self.color('#f0f')
    self.speed = 1.5
    self.goto(random.randint(-256, 256), random.randint(-256, 256))
    self.setheading(random.randint(0, 360))
  
  def jump(self):
    self.goto(random.randint(-256, 256), random.randint(-256, 256))
    self.setheading(random.randint(0, 360))
  
  def move(self):
    self.forward(self.speed)
    if self.xcor() > 300:
      self.setx(-300)
    
    if self.xcor() < -300:
      self.setx(300)
    
    if self.ycor() > 300:
      self.sety(-300)
    
    if self.ycor() < -300:
      self.sety(300)

class Border(Turtle):
  def __init__(self):
    Turtle.__init__(self)
    self.penup()
    self.speed(0)
    self.color('#fff')
    self.pensize(10)
  
  def draw_border(self):
    self.penup()
    self.goto(-300, -300)
    self.pendown()
    self.goto(-300, 300)
    self.goto(300, 300)
    self.goto(300, -300)
    self.goto(-300, -300)
    self.hideturtle()

player1 = Hero()
player2 = Hero()
monster = Monster()
border = Border()
listen()
onkeypress(player1.l, "Left")
onkeypress(player1.r, "Right")
onkeypress(player1.u, "Up")
onkeypress(player1.d, "Down")
onkeypress(player1.l, "a")
onkeypress(player1.r, "d")
onkeypress(player1.u, "w")
onkeypress(player1.d, "s")
onkeypress(player1.accel, "o")
onkeypress(player1.decel, "l")
onkeypress(player2.accel, "q")
onkeypress(player2.decel, "e")

onkey(player1.spin, "Escape")

border.draw_border()
while True:
  if player1.distance(monster) < 20 or player2.distance(monster) < 20:
    monster.jump()
  player1.move()
  player2.move()
  monster.move()