#把输入的姓名，显示到海龟画图中

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green"]

#弹出输入框，让用户输入一个字符串
your_name = turtle.textinput("Input your full name","What is your name？")

#把刚才输入的姓名，画到海龟螺旋线上
for x in range(100):
    t.pencolor(colors[x%4])
    t.penup()               #把画笔抬起离开屏幕，这样就保证执行下一句（t.forward(x*4)）时，屏幕上不会画上常规的螺旋线
    t.forward(x*4)          #使画笔向前移动x*4的距离
    t.pendown()             #把画笔放下，准备在屏幕上画画
    t.write(your_name,font=("Arial",int((x+4)/4),"bold"))  #在屏幕上写出刚才输入的名字
    t.left(92)              #把画笔转向92度
