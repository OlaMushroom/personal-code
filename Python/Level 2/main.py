# Level 2:
# 8/11/2020:
# Switch variable:
'''
a = str(input('a: '))
b = str(input('b: '))
c = a
a = b
b = c
print('a =',a)
print('b =',b)
'''

#15/11/2020:
#Print even number only:
'''
def even():
    i = 0
    while (0 <= i <= 100):
      if i % 2 == 0:
        print(i)
      i += 1
even()
'''

#Factorial:
'''
def factorial():
  a = 1
  n = int(input('Hãy cho 1 số nguyên bất kì để tính giai thừa: '))
  for i in range (1,n + 1):
    a = a * i
  if n == 0:
    a = 1
  if n < 0:
    print('Không có giai thừa cho số',n)
  print('Giai thừa của',n,'là',a)
factorial()
'''

#Calculation:
'''
def add():
  print(a + b)
def minus():
  print(a - b)
def multiply():
  print(a * b)
def divide():
  print(a / b)
a = float(input('Hãy nhập số #1: '))
b = float(input('Hãy nhập số #2: '))
c = int(input('Hãy chọn kiểu tính\n1. Cộng\n2. Trừ\n3. Nhân\n4. Chia\nLựa chọn: '))
if c == 1:
  add()
elif c == 2:
  minus()
elif c == 3:
  multiply()
elif c == 4:
  divide()
else:
 c = int(input('Lựa chọn này không hợp lệ, hãy cho lựa chọn khác: '))
'''

#22/11/2020:
#Hàm tính toán:
'''def sum (a,b):
  return(a+b)
def input0():
  a = float(input('Nhập số a: '))
  b = float(input('Nhập số b: '))
  print(sum(a,b))
input0()'''

#Hàm tính tổng:
'''def sum(*num):
  s = 0
  for i in num:
    s += i
  return s
print(sum(1,2,3,4,5,6,7,8,9))'''

#29/11/2020:
#Module tính toán:
'''import Math as a
b = a.sum(2,3)
print(b)'''

'''def sum(a,b):
  return a + b
def minus(a,b):
  return a - b

def prime(num):
    primes = []
    for i in range(2, num + 1):
        is_p = True
        for p in primes:
            if not i % p:
                is_p = False
                break
        if is_p:
            primes.append(i)
    print(primes)
    return primes

def gcd(a, b):
    m = min(a, b)
    n = max(a, b) % m
    return gcd(m, n) if n else m
    
def lcm(a, b):
    return int(a * b / gcd(a, b))

print(lcm(3, 5))'''

#Module ngẫu nhiên chọn số bất kì:
'''import random as a
b = a.randrange(1,100)
print(b)'''

#Module ngẫu nhiên chọn số bất kì nâng cao:
'''import random
list = [2,333,1111,564464]
a = random.randrange(100)
b = random.randrange(0,100)
c = random.randrange(0,100,4)
d = random.randint(0,100)
e = random.uniform(0,100)
f = random.choice(list)
g = random.sample(list,2)
random.shuffle(list)
print(a,'\n',b,'\n',c,'\n',d,'\n',e,'\n',f,'\n',g,'\n',list)'''

#6/12/2020:
#Thao tác với file:
'''f = open("hien.txt","w")
f.write("Hiển đầu cắt moi")
f.close()'''

'''f = open("hien.txt","r")
a = f.readlines()
f.close()
f = open("hien.txt","w")
for i in a:
  if i != "abc"+"\n":
    f.write(i)
f.close()'''

'''import os
os.remove("a.txt")
os.rmdir("a")'''

#13/12/2020:
'''import turtle
t = turtle.Screen()
t.bgcolor('#000000')
s = turtle.Turtle()
s.shape("arrow")
s.width(1)
s.color("#ffffff")
s.speed(10)
s.goto(0,0)
for i in range (999):
  s.forward(100)
  s.right(181)
s.penup()
s.pendown()'''

#20/12/2020:
'''
import turtle as t
s = t.Screen()
s.setup(500,281)
s.bgpic("bg.gif")
t.shape("turtle")
t.color("red")
t.penup()
def char():
  p = "hr.gif"
  t.addshape(p)
  t.shape(p)

def forward():
  t.forward(10)
def backward():
  t.backward(10)
def left():
  t.left(10)
def right():
  t.right(10)
s.onkey(forward,"w")
s.onkey(backward,"s")
s.onkey(left,"a")
s.onkey(right,"d")
s.listen()
'''

#3/1/2021:
'''#Game config:
import turtle as t
import math as m
import random as r
sc = t.Screen()
sc.setup(500,281)
sc.bgpic("level2/bg.gif")

#Player:
p = t.Turtle()
p.shape("turtle")
p.color("yellow")
p.penup()
speed = 0

#Gamerule:
def left():
  p.left(10)
def right():
  p.right(10)
def inc_speed():
  global speed
  speed += 1
  if speed >= 5:
    speed = 5
def dec_speed():
  global speed
  speed -= 1
  if speed <= -5:
    speed = -5

t.onkey(inc_speed,"Up")
t.onkey(dec_speed,"Down")
t.onkey(left,"Left")
t.onkey(right,"Right")
t.listen()

#Goal:
g = t.Turtle()
img = "level2/hr.gif"
sc.addshape(img)
g.shape(img)
g.penup()
g.speed(0)
g.setposition(r.randint(-180,180),r.randint(-90,90))

#Collision:
def hit(x,y):
  dstnc = m.sqrt(m.pow(x.xcor()-y.xcor(), 2) + m.pow(x.ycor()-y.ycor(), 2))
  if dstnc < 25:
    return True
  else:
    return False

#Hit edge:
def edge(e):
  if (e.xcor()<-200) or (e.xcor()>200):
    t.left(180)
  if (e.ycor()<-100) or (e.ycor()>100):
    t.left(180)

#Run & stop:
while True:
  p.forward(speed)
  edge(p)
  g.forward(10)
  g.left(r.randint(10, 180))
  edge(g)
  if hit(p,g):
    print("You win!")
    break'''

#Level 2 project:
'''import math, random
from turtle import *
s = Screen()
s.setup(700, 700)
s.bgcolor('#000')
s.title('Hello')

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
# player2 = Hero()
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
# onkeypress(player2.accel, "q")
# onkeypress(player2.decel, "e")

onkey(player1.spin, "Escape")

border.draw_border()
while True:
  if player1.distance(monster) < 20:
  #  or player2.distance(monster) < 20:
    monster.jump()
  player1.move()
  # player2.move()
  monster.move()'''

#Project cuối khóa:
#Bắt rùa
import math, random
from turtle import *
s = Screen()
s.setup(700, 700)
s.bgcolor('#000')
s.title('Hello')

player = Turtle()
player.penup()
player.speed(0)
player.shape('circle')
player.color('red')
player.speed = 3

#kiểm tra và đặt lại vị trí cho nhân vật khi chạm biên
def player_move():
  player.forward(player.speed)
  if player.xcor() > 290: player.setx(-290)
  if player.xcor() < -290: player.setx(290)
  if player.ycor() > 290: player.sety(-290)
  if player.ycor() < -290: player.sety(290)

#đặt hướng đi của nhân vật
def l():
  while player.heading() != 180: player.setheading(180)
def r():
  if player.heading() != 0: player.setheading(0)
def f():
  if player.heading() != 90 : player.setheading(90)
def b():
  if player.heading() != 270: player.setheading(270)

#đặt hàm tăng và giảm tốc cho nhân vật
def accel(): 
  player.speed += 1
def decel(): 
  player.speed -= 1

monster = Turtle()
monster.penup()
monster.speed(0)
monster.shape('turtle')
monster.color('yellow')
monster.speed = 1

#cho rùa quay và đi tới vị trí ngẫu nhiên:
monster.goto(random.randint(-256, 256), random.randint(-256, 256))
monster.setheading(random.randint(0, 360))

#Đặt rùa ở vị trí khác khi nhân vật chạm rùa
def monster_jump():
  monster.goto(random.randint(-256, 256), random.randint(-256, 256))
  monster.setheading(random.randint(0, 360))

#kiểm tra và đặt lại vị trí cho rùa khi chạm biên
def monster_move():
  monster.forward(monster.speed)
  if monster.xcor() > 290: monster.setx(-290)
  if monster.xcor() < -290: monster.setx(290)
  if monster.ycor() > 290: monster.sety(-290)
  if monster.ycor() < -290: monster.sety(290)

#tạo vạch kẻ cho biên
border = Turtle()
border.penup()
border.speed(0)
border.color('#fff')
border.pensize(10)
border.penup()
border.goto(-300, -300)
border.pendown()
border.goto(-300, 300)
border.goto(300, 300)
border.goto(300, -300)
border.goto(-300, -300)
border.hideturtle()

#nhận lệnh từ bàn phím của người chơi
listen()
onkeypress(l, "a")
onkeypress(r, "d")
onkeypress(f, "w")
onkeypress(b, "s")
onkeypress(accel, "1")
onkeypress(decel, "0")

#chạy,dừng và tính điểm:
a = 0
print('Chào mừng đến với game "Bắt rùa"\nBạn sẽ là hình tròn có màu đỏ còn rùa sẽ có màu vàng\nMỗi lần bạn bắt được con rùa, nó sẽ chuyển vị trí, còn bạn sẽ được 1 điểm và bạn sẽ thắng nếu bạn được 5 điểm')
while True:
  player_move()
  monster_move()
  if player.distance(monster) < 20: 
    monster_jump()
    a += 1
    print("Điểm của bạn:",a)
  if a == 5:
    print('Bạn đã thắng!')
    break