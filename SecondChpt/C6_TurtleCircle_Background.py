#海龟画圆 - 四色螺旋 -添加背景色
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
colors = ["red","green","blue","orange"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(91)
