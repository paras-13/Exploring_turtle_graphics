# To print Olympic Symbol using python turtle module
import turtle as t

t.bgcolor("cyan")
t.pensize(5)
t.speed(10)
t.hideturtle()
def move_pen(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

t.color("blue")
move_pen(-110,-25)
t.circle(45)

t.color("black")
move_pen(0,-25)
t.circle(45)

t.color("red")
move_pen(110,-25)
t.circle(45)

t.color("yellow")
move_pen(-55,-75)
t.circle(45)

t.color("green")
move_pen(55,-75)
t.circle(45)

move_pen(-100,120)

t.pensize(1)
t.color("black")
t.write("Olympic symbol",font = ("Times",20,"bold"))
t.done()