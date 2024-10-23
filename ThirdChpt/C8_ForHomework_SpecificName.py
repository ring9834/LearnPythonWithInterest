#编程挑战：让用户输入螺旋线有几个边，然后询问他们的名字
import turtle
turtle.bgcolor("black")
t = turtle.Pen()

#sides = 7
sides = int(turtle.numinput("Number of Edge","Numbers of Edge","Please input the number of edges you want（between 1 and 8）",4,1,8))

#弹出输入框，让用户输入一个字符串
your_name = turtle.textinput("Input your full name","What is your name？")

colors = ["red","green","blue","orange","purple","yellow","white","gray"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.penup()
    t.forward(x * 3/sides + x)
    t.pendown()             #把画笔放下，准备在屏幕上画画
    t.write(your_name,font=("Arial",int((x+4)/4),"bold"))  #在屏幕上写出刚才输入的名字
    t.left(360/sides + 1)
    t.width(x * sides/200)
