
# Sinchain 
import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
s.title("Sinchain")
s.bgcolor("pink")
turtle.screensize(canvwidth=400, canvheight=800)
t.speed(15)
# Short
t.pensize(2)
t.color("black","yellow")
t.begin_fill()
t.rt(25)
t.fd(20)
t.rt(40)
t.fd(30)
t.lt(65)
t.fd(120)
t.lt(95)
t.fd(90)
t.lt(85)
t.fd(250)
t.lt(85)
t.fd(90)
t.lt(95)
t.fd(132)
t.lt(90)
t.fd(30)
t.end_fill()


t.lt(180)
t.fd(30)
t.rt(90)
t.fd(45)

#  Left Leg
t.color("black","orange")
t.begin_fill()
t.lt(85)
t.fd(90)
t.rt(85)
t.fd(30)
t.rt(90)
t.fd(89)
t.rt(90)
t.fd(40)
t.end_fill()

t.penup()
t.goto((-35.73,-125.30))
t.pendown()

t.color("black","white")            # Left leg shock
t.begin_fill()
t.rt(95)
t.fd(30)
t.rt(85)
t.fd(26)
t.rt(85)
t.fd(30)
t.end_fill()

t.penup()
t.goto(-38.34,-155.19)
t.pendown()

# Left leg shoe
t.color("black","black")
t.begin_fill()
t.rt(95)
t.fd(5)
t.rt(75)
t.fd(18)
t.rt(100)
t.fd(80)
t.rt(145)
t.fd(40)
t.lt(40)
t.fd(17)
t.rt(65)
t.fd(15)
t.rt(105)
t.fd(20)
t.end_fill()

# Right Leg
t.penup()
t.goto(30.80,-35.64)
t.pendown()
t.lt(90)
t.fd(40)
t.color("black", "orange")
t.begin_fill()
t.rt(85)
t.fd(90)
t.lt(85)
t.fd(30)
t.lt(88)
t.fd(89)
t.lt(90)
t.fd(40)
t.end_fill()

t.penup()
t.goto(78.64,-125.30)
t.pendown()

# Right leg shock
t.color("black","white")
t.begin_fill()
t.lt(97)
t.fd(30)
t.lt(85)
t.fd(26)
t.lt(85)
t.fd(30)
t.end_fill()

t.penup()
t.goto(81.25,-155.19)
t.pendown()

# Right leg Shoe
t.color("black","black")
t.begin_fill()
t.lt(95)
t.fd(5)
t.lt(75)
t.fd(18)
t.lt(100)
t.fd(80)
t.lt(145)
t.fd(40)
t.rt(40)
t.fd(17)
t.lt(65)
t.fd(15)
t.lt(105)
t.fd(20)
t.end_fill()

# t.showturtle()

t.penup()
t.goto(-107.04,54.02)
t.pendown()

# T-Shirt
t.color("black","red")
t.begin_fill()
t.rt(90)
t.fd(8)
t.rt(100)
t.fd(110)
t.bk(15)
t.lt(60)
t.fd(110)
t.rt(65)
t.fd(10)         #
t.rt(15)
t.fd(20)
t.rt(90)
t.fd(150)
t.lt(30)
t.fd(125)
t.lt(10)
t.fd(20)
t.lt(10)
t.fd(20)
t.lt(15)
t.fd(90)
t.rt(95)
t.fd(30)
t.rt(70)
t.fd(105)
t.lt(40)
t.fd(80)
t.end_fill()

# Face

# print(a)
# print(a)
turtle.mainloop()