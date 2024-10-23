#字符串列表 - 另一种变量
import turtle
turtle.bgcolor("black")
t = turtle.Pen()

#sides = 7
sides = int(turtle.numinput("Number of Edge","Please input the number of edges you want（between 1 and 8）",4,1,8))

colors = ["red","green","blue","orange","purple","yellow","white","gray"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x * sides/200)
