#海龟画图 - 一个变量搞定一切
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
sides = 6
colors = ["red","green","blue","orange","purple","yellow"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x * sides/200)
