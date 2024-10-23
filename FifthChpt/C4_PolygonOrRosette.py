import turtle
t = turtle.Pen()
number = int(turtle.numinput("Input Number","Plese input the number of polygon or circle：",6))
shape = turtle.textinput("Please select what you want to draw","Input ‘p’ for polygon，Input ‘r’ for circle：")
for x in range(number):
    if shape == 'r':
        t.circle(100)
    else:
        t.forward(150)
    t.left(360/number)
