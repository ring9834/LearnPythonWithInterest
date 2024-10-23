import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")
sides = int(turtle.numinput("Number of Edge","Please input the number of small spirial line",4,2,6))
colors = ["red","yellow","blue","green","pink","orange"]

for m in range(100):
    t.forward(m*4)
    position = t.position()
    heading = t.heading()
    print(position,heading)

    for n in range(int(m/2)):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.forward(n*2)
        t.right(360/sides - 2)
        t.penup()

    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360/sides + 2)
