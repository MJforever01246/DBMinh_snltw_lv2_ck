import turtle
import time
import random
import math
import threading
wn=turtle.Screen()
wn.title('Flappy Bird')
wn.bgcolor('black')
wn.bgpic('screen.gif')
wn.addshape('bird.gif')
wn.addshape('pipe.gif')

class bird(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape('square')
        self.color('blue')
        self.speed(0)
        self.goto(-200, 200)
        self.dx=0
        self.dy=1
    def go_up(self):
        self.dy+=19
        if self.dy>8:
            self.dy=11

class ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.color("green")
        self.hideturtle()
        self.setheading(180)
        self.showturtle()
    def reposition(self):
        self.hideturtle()
        x = random.randint(200, 300)
        y =  random.randint(-270, 270)
        self.showturtle()
        self.setposition(x, y)
        self.setheading(180)
    def move(self):
        self.forward(20)
def collision_b1_b4(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<29:
        return True
    else:
        return False
    
gravity=-1.5
wn.listen()
player = bird()
wn.onkey(player.go_up,'space')

number_of_bird3 = 6
bird3 = []

for i in range(number_of_bird3):
    bird3.append(ball())
for bird4 in bird3:
    x = random.randint(20, 320)
    y =  random.randint(20, 270)
    bird4.setposition(x, y)
Game_over= False
while True:
    gravity=-1.5
    '''for bird4 in bird3:
        bird4.move()
        if bird4.xcor()<= -320:
            bird4.reposition()'''
    player.shape('bird.gif')
    time.sleep(0.01)
    wn.update()
    player.dy+= gravity
    y = player.ycor()
    y += player.dy
    player.sety(y)
    if y < -564:
        print("die")
    for bird4 in bird3:
        bird4.move()

        #collison
        if collision_b1_b4(player,bird4):
            Game_over= True
        if Game_over==True:
            player.hideturtle()
            for bird4 in bird3:
                bird4.hideturtle()
            wn.bgpic('gameover.gif')
            break
        if bird4.xcor()<-400:
            bird4.hideturtle()
            x=random.randint(200, 320)
            y =  random.randint(20, 270)
            bird4.goto(x,y)
            bird4.showturtle()
delay = input("Press enter to finish")

