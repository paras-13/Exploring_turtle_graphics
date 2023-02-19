# Background blinker
import turtle
import time
s = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.goto(-150,0)
t.pendown()
s.bgcolor("white")
t.write("Hello welcome to the world of programming",font=("Times",20,"bold"))
lst = ['blue','orange','cyan','brown','yellow','violet','indigo',"red"]
while True:
    for i in range(8):
        s.bgcolor(lst[i])
turtle.mainloop()
