# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
with open('drawing.txt') as f:
    for line in f:
        lineCleared = line.split()

# wait
turtle.Screen().exitonclick()

