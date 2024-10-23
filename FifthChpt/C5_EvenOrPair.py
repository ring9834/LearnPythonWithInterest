import turtle
t = turtle.Pen()
sides = int(turtle.numinput("Input Number","Please input the number of edge for the spirial graph：",4))
for m in range(5,75):
    t.left(360/sides + 2)
    #t.width(m/55 + 1)
    t.width(1)
    t.penup()
    t.forward(m*3)
    t.pendown()
    if(m%2 == 0):
        for n in range(sides):
            t.circle(m/3)
            t.right(360/sides)
    else:
        for n in range(sides):
            t.forward(m)
            t.right(360/sides)
