import turtle
import random
import math


sc=turtle.Screen()
sc.bgpic("space.gif")
mypen=turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
mypen.speed(0)
for i in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()
player=turtle.Turtle()
image="sieunhan.gif"
sc.addshape(image)
player.shape(image)
player.penup()
player.setposition(0,-250)
player.setheading(90)
player.speed=15
#úm ba la xì bùa quái vật
enemy= turtle.Turtle()
image="quaivat.gif"
sc.addshape(image)
enemy.shape(image)
enemy.penup()
enemy.speed()
enemy.setposition(random.randint(-300, 300),random.randint(-100,300))
enemyspeed=2
bullet=turtle.Turtle()
bullet.color("black")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed=20
bullet="ready"
sung=turtle.Turtle()
sung.color("brown")
sung.shape("circle")
sung.penup()
sung.speed(0)
sung.setheading(90)
sung.hideturtle()
bulletstate_quaivat="ready"
bulletspeed_quaivat=20
def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()
#vu khi cua quai vat
def fire_bullet_quaivat():
    global bulletstate_quaivat
    if bulletstate_quaivat == "ready":
        bulletstate_quaivat == "fire"
        x=enemy.xcor()
        y=enemy.ycor()+10
        sung.setposition(x,y)
        sung.showturtle()

#dinh nghia cac phim di chuyen
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < - 280:
        x = -280
    player.setx(x)
    
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
# khi nhan phim
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")
turtle.listen()
#kiem tra va cham
def isCollision(t1,t2):
    #tinh khoang cach
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if d<20:
        return True
    else:
        return False
#tao ham kiem tra nhan vat khi va cham bien
def boundaryChecking(t):
    if t.xcor()<-300 or t.xcor()>300:
        t.right(180)
        t.setposition(random.randint(-300,300),random.randint(-300,300))
    if t.ycor()<-300 or t.ycor()>300:
        t.right(180)
        t.setposition(random.randint(-300,300),random.randint(-300,300))

#main game loop
while True:
    #thiet lap di chuyen cua quai vat
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #Goi ham khoi tao vu khi va su dung
    fire_bullet_quaivat()
    #dieu khien huong di dan cua quai vat
    if(bulletstate_quaivat == "fire"):
        y = sung.yor()
        y -= bulletspeed_quaivat
        sung.sety()
    #kiem tra dan vi tri bottom, neu dung thi an dan
    if sung.ycor()<-275:
        sung.hideturtle()
        bulletstate_quaivat = "ready"

    #Move the enemy back and down
    if enemy.xcor()>280:
        #move all enemies down
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
        #change enemy direction
        enemyspeed *= -1
    if enemy.xcor()<-280:
        #move all enemies down
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
        #change enemy direction
        enemyspeed *= -1
        
    #kiem tra va cham giua dan cua sieu anh hung va quai vat
    if isCollision(bullet,enemy):
        #reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0,-400)
        #reset the enemy
        x = random.randint(-200,200)
        y = random.randint(100,250)
        enemy.setposition(x,y)

    #kiem tra va cham giua dan cua quai vat va sieu anh hung
    if isCollision(sung,player):
        #reset the bullet
        sung.hideturtle()
        bulletstate_quaivat = "ready"
        bullet.setposition(0,-400)
        #reset the enemy
        x = random.randint(-200,200)
        y = random.randint(100,250)
        enemy.setposition(x,y)

    #kiem tra dan cua sieu anh hung
    if(bulletstate == "fire"):
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    #neu dan cua sieu anh hung di chuyen len dinh thi an di
    if bullet.yor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"











        
