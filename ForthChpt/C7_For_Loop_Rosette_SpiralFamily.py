import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","orange","purple","white","brown","pink","gray"]
family = []
name = turtle.textinput("My familily","Plase input a name，or press ENTER key to exit.")
while name != "":
    family.append(name)
    name = turtle.textinput("My familily","Plase input a name，or press ENTER key to exit.")

for x in range(100):
    t.pencolor(colors[x%len(family)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)],font=("Arail",int((x+4)/4),"bold"))
    t.left(360/len(family)+5)
