import turtle as t
import random
import time

point = 0
start_time = time.time()
use_time = 0
x = random.randint(-300, 300)
y = random.randint(-300, 300)

game = t.Screen()
game.setup(700, 700)
game.bgpic('tenor.gif')
t.tracer(2)

pen = t.Turtle()
pen.ht()
pen.up()
pen.setpos(200, 260)
pen.color('red')

def update_time():
    global use_time
    now_time = time.time()
    use_time = int(now_time - start_time)
    time_str = 'Time' +':'+ str(use_time)
    pen.clear()
    pen.write(time_str, align="left", font=('Arial', 20, 'bold'))

po = t.Turtle()
po.ht()
po.up()
po.setpos(-250, 260)
pen.color('yellow')
def update_point():
    point_str = 'Point' +':'+str(point)
    po.clear()
    po.write(point_str, align="left", font=('Arial', 20))

rat_number = 2
rats = []
t.register_shape('p.gif')
for i in range(rat_number):
    rat = t.Turtle()
    rat.ht()
    rat.up()
    rat.speed(0)
    rat.left(random.randint(0, 360))
    rat.shape('p.gif')
    rat.setpos(x, y)
    rat.showturtle()
    rats.append(rat)

cat = t.Turtle()
cat.color("yellow")
cat.shapesize(2, 2)
cat.up()
cat.speed(1)
def move_left():
    cat.left(15)
def move_right():
    cat.right(15)
def speedup():
    global cat_speed
    cat_speed += 1
def speeddown():
    global cat_speed
    cat_speed -= 1

t.listen()
t.onkey(move_left, 'Left')
t.onkey(move_right, 'Right')
t.onkey(speedup, 'Up')
t.onkey(speeddown, 'Down')

def catch(rat):
    global point
    if cat.distance(rat) < 30:
        rat.ht()
        rats.remove(rat)
        point += 1

cat_speed = 1
while True:
    update_time()
    update_point()
    cat.fd(cat_speed)
    x = cat.xcor()
    if x>330 or x<-350:
        cat.left(180)
    y = cat.ycor()
    if y<-350 or y>350:
        cat.right(180)
    for rat in rats:
        rat.fd(1)
        catch(rat)
        x = rat.xcor()
        y = rat.ycor()
        if x > 330 or x < -350:
            rat.left(180)
        y = rat.ycor()
        if y < -350 or y > 350:
            rat.right(180)
        if len(rats) == 0:
            p = t.Turtle()
            p.ht()
            p.up()
            p.setpos(-100, 0)
            p.color('red')
            p.write('Game Over'+ ',Point: '+str(point)+', '+'Time'+':'+str(use_time), align='left', font = ('Arial', 18, 'bold'))
            break
game.mainloop()