#printing maze

import turtle

def printing(row,col,walls):
    t=turtle.Turtle()
    x1=-380
    y1=-x1
    size=((2*(-x1))/row)
    t.clear()
    t.speed(0)
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(-x1,y1)
    t.goto(-x1,-y1)
    #t.setheading(0)
    for i in range(row):
        t.penup()
        t.goto(x1,-y1+size*(i))
        for j in range(col):
            if(walls[i][j][3]==1):
                t.pendown()
            else:
                t.penup()
            t.forward(size)
    t.left(90)
    for i in range(row):
        t.penup()
        t.goto(x1+size*(i),-y1)
        for j in range(col):
            if(walls[j][i][0]==1):
                t.pendown()
            else:
                t.penup()
            t.forward(size)