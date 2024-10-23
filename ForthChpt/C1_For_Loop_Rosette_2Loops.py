import turtle
t = turtle.Pen()
numbers_of_circles1 = 30
turtle.bgcolor("black")
t.pencolor("green")
for x in range(numbers_of_circles1):
  t.circle(150)
  t.left(360/numbers_of_circles1)

numbers_of_circles2 = 40
t.pencolor("yellow")
for x in range(numbers_of_circles2):
  t.circle(60)
  t.left(360/numbers_of_circles2)

