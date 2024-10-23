import turtle
t = turtle.Pen()
numbers_of_circles = int(turtle.numinput("Number of Circle","Please input the number of circle you want.",6)) #默认为6个
for x in range(numbers_of_circles):
  t.circle(150)
  t.left(360/numbers_of_circles)

