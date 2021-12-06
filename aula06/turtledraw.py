# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
with open('drawing.txt') as f:
    for line in f:
        line = line.strip('\n')
        print('Reading text:', line)
        if line == 'UP': 
            t.up()
        elif line == 'DOWN': 
            t.down()
        else:
            splitCoords = line.split()
            coordX, coordY = float(splitCoords[0]), float(splitCoords[1])
            t.goto(coordX, coordY)

# wait
turtle.Screen().exitonclick()

