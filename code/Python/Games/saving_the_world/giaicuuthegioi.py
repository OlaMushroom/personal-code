import turtle
import random
import math
import winsound
screen = turtle.Screen()
screen.setup(400, 400)
#thiết lập hình ảnh nền cho màn hình đồ họa
screen.bgpic("space.gif")
#image = "tau.gif"
#screen.addshape(image)
#turtle.shape(image)

mypen=turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
mypen.speed()
for i in range(4):
    mypen.forward(600)
    mypen.left(90)
#vẽ xong, ẩn đối tượng vẽ
mypen.hideturtle()
#tao nhan vat sieu anh hung (rua)
player = turtle.Turtle()
player.color("yellow")
player.shape("turtle")
#thiet lap khong ve khi di chuyen
player.penup()

#thiết lập tốc độ siêu anh hùng
speed = 1
#định nghĩa các phím ra chuyển
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
#ham tang toc do
def increaseSpeed():
    global speed
    speed += 1
    if speed>=5:
       speed=5
#ham giam toc doc
def decreaseSpeed():
    global speed
    speed -=1
    if speed<= -5:
       speed = -5
#khi nhan phim
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increaseSpeed, "Up")
turtle.onkey(decreaseSpeed, "Down")
#tao ra quai vat
goal = turtle.Turtle()
image = "quaivat.gif"
screen.addshape(image)
goal.shape(image)
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-300,300),random.randint(-300,300))
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

#vong lap game
while True:
    #thiet lap sieu anh hung di ve phia truoc
    player.forward(speed)
    #kiem tra sieu nhan hung co cham bien
    boundaryChecking(player)
    #kiem tra va cham
    if isCollision(player,goal):
        print("win - giai cuu the gio")
        screen.bgpic("thewin.gif")
        winsound.PlaySound("explosion.wav",winsound.SND_FILENAME)
        break
    #thiet lap quai vat di chuyen
    goal.forward(10)
    goal.left(random.randint(10,180))
    #kiem tra quai vat co cham bien
    boundaryChecking(goal)
