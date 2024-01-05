import turtle
def displayroute(coordinate,startx,starty,gridsize):
    turtle.speed(0)
    turtle.penup()
    x=startx+gridsize/2
    y=starty+gridsize/2
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pensize(gridsize/4)
    turtle.color("palegreen")
    for a in range(len(coordinate)-1):
        x=x+(coordinate[a+1][0]-coordinate[a][0])*gridsize
        y=y+(coordinate[a+1][1]-coordinate[a][1])*gridsize
        turtle.goto(x,y)
