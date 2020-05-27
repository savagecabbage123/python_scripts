from turtle import *
from random import randint
speed(5)
penup()
goto(-140, 140)
for step in range(12):
    write(step, align="center")
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
#make a turtle named tim
tim = Turtle()
tim.color("red")
tim.shape("turtle")
tim.penup()
tim.goto(-165, 100)
tim.pendown()

jim = Turtle()
jim.color("blue")
jim.shape("turtle")
jim.penup()
jim.goto(-165, 70)
jim.pendown()

patrick = Turtle()
patrick.color("pink")
patrick.shape("turtle")
patrick.penup()
patrick.goto(-165, 40)
patrick.pendown()

for turn in range(1):
    tim.right(360)
    jim.right(360)
    patrick.right(360)
    
for turn in range(90):
    tim.forward(randint(1,5))
    jim.forward(randint(1,5))
    patrick.forward(randint(1,5))
