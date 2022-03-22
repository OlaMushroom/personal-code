import turtle
import os
import math
import random
import winsound
import time
#-------------------------
# Khai bao over game
over_pen = turtle.Turtle()
over_pen.speed(0)
over_pen.color("yellow")
over_pen.penup()
over_pen.setposition(-200,50)
over_pen.hideturtle()

# Khai bao player win
win_pen = turtle.Turtle()
win_pen.speed(0)
win_pen.color("yellow")
win_pen.penup()
win_pen.setposition(-200,50)
win_pen.hideturtle()

# thiết lập màn hình đồ họa và hình ảnh nền
sc = turtle.Screen()
sc.bgpic("space.gif")

# Vẽ vùng giới hạn di chuyển:
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
mypen.speed(0)
for i in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Tạo ra nhân vật siêu anh hùng
player = turtle.Turtle()
image="sieunhan.gif"
sc.addshape(image)
player.shape(image)
player.penup()
player.setposition(0, -250)
player.setheading(90)
playerspeed = 15
bulletspeed = 20
#trang thai sung Sieu anh hùng
bulletstate = "ready"

#---------------------------
# Tao ra quai vat
bulletspeed_quaivat = 20
enemy = turtle.Turtle()
image="quaivat.gif"
sc.addshape(image)
enemy.shape(image)
enemy.penup()
enemy.speed(0)
enemy.setposition(random.randint(-300, 300), random.randint(-100, 300))
enemyspeed = 2
bulletstate_quaivat="ready"

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

#sung cua quai vat
sung = turtle.Turtle()
sung.color("red")
sung.shape("circle")
sung.penup()
sung.speed(0)
sung.setheading(90)
sung.shapesize(0.5, 0.5)
sung.hideturtle()

# ham tinh thoi gian
value = time.time ()
def stopWatch(value):
    
    valueD = (((value/365)/24)/60)
    Days = int (valueD)

    valueH = (valueD-Days)*365
    Hours = int(valueH)

    valueM = (valueH - Hours)*24
    Minutes = int(valueM)

    valueS = (valueM - Minutes)*60
    return int(valueS)

#Draw timer
time_pen = turtle.Turtle()
time_pen.speed(0)
time_pen.color("yellow")
time_pen.penup()
time_pen.setposition(-20, 260)
end_giay =time.time ()
giay=stopWatch(end_giay-value)
timestring = str(giay)
time_pen.write(timestring, False, align="left", font= ("Arial", 20, "normal"))
time_pen.hideturtle()

#Set the score to 0 and draw the score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Player: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#score quai vat
score_quaivat = 0
score_pen_quaivat = turtle.Turtle()
score_pen_quaivat.speed(0)
score_pen_quaivat.color("white")
score_pen_quaivat.penup()
score_pen_quaivat.setposition(200, 280)
scorestring_quaivat = "Enemy: %s" %score_quaivat
score_pen_quaivat.write(scorestring_quaivat, False, align="left", font=("Arial", 14, "normal"))
score_pen_quaivat.hideturtle()   

# định nghĩa các phím ra chuyển
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = - 280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    
    if (distance<20):
        return True
    else:
        return False
    
def boundaryChecking(t):
    if t.xcor() < -300 or t.xcor() > 300:
        t.right(180)
        t.setposition(random.randint(-300, 300), random.randint(-300, 300))
    if t.ycor() < -300 or t.ycor() > 300:
        t.right(180)
        t.setposition(random.randint(-300, 300), random.randint(-300, 300))

# Sung cua Sieu Nhan
def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
          #winsound.PlaySound('laser.wav', winsound.SND_FILENAME)
          #os.system("laser.wav")
          bulletstate = "fire"
          #Move the bullet to the just above the player
          x = player.xcor()
          y = player.ycor() + 10
          bullet.setposition(x, y)
          bullet.showturtle()

# Sung cua quai vat
def fire_bullet_quatvat():
    #Declare bulletstate as a global if it needs changed
    global bulletstate_quaivat
    if bulletstate_quaivat == "ready":
          #winsound.PlaySound('laser.wav', winsound.SND_FILENAME)
          #os.system("laser.wav")
          bulletstate_quaivat = "fire"
          #Move the bullet to the just above the player
          x = enemy.xcor()
          y = enemy.ycor() + 10
          sung.setposition(x, y)
          sung.showturtle()

# khi nhấn phím
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
turtle.listen()

#Main game loop
while True:
    #update time
    end_giay =time.time ()
    giay=stopWatch(end_giay-value)
    timestring = str(giay)
    time_pen.clear()
    time_pen.write(timestring, False, align="left", font= ("Arial", 20, "normal"))
    time_pen.hideturtle()
        
    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    # quai vat ban
    fire_bullet_quatvat()
    if (bulletstate_quaivat == "fire"):
            y = sung.ycor()
            y -= bulletspeed_quaivat
            sung.sety(y)
                
    #Check to see if the bullet has gone to the botton
    if sung.ycor() < -275:
            sung.hideturtle()
            bulletstate_quaivat = "ready"

#Move the enemy back and down
    if enemy.xcor() > 280:
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)
            #Change enemy direction
            enemyspeed *= -1
		
    if enemy.xcor() < -280:
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)
            #Change enemy direction
            enemyspeed *= -1

    #Check for a collision between the bullet and the enemy
    if isCollision(bullet, enemy):
            winsound.PlaySound('explosion.wav', winsound.SND_FILENAME)
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update the score
            score += 10
            scorestring = "Player: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
		
    #va cham giua Dan va sieu anh hung
    if isCollision(sung, player):
            winsound.PlaySound('explosion.wav', winsound.SND_FILENAME)
            
           #Reset the bullet
            sung.hideturtle()
            bulletstate_quaivat = "ready"
            bullet.setposition(0, -400)

           #Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            
            #Update the score
            score_quaivat += 10
            scorestring_quaivat = "Enemy: %s" %score_quaivat
            score_pen_quaivat.clear()
            score_pen_quaivat.write(scorestring_quaivat, False, align="left", font=("Arial", 14, "normal"))

    # va cham nguoi choi va quai vat        
    if isCollision(player, enemy):
            winsound.PlaySound('explosion.wav', winsound.SND_FILENAME)
            #os.system("afplay explosion.wav&")
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")
            break

    #Move the bullet
    if (bulletstate == "fire"):
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)
                
    #Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"

    if giay>=59:
        if score_quaivat>=score:
            sc.bgpic("over.gif")
            winsound.PlaySound('over.wav', winsound.SND_FILENAME)
            over_pen.write("YOU ARE LOST!!!", False, align="left", font=("Arial", 40, "normal"))
            break
        else:
            sc.bgpic("over.gif")
            winsound.PlaySound('over.wav', winsound.SND_FILENAME)
            win_pen.write("YOU ARE WIN!!!", False, align="left", font=("Arial", 40, "normal"))
            break
