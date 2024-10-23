answer = input("Do you want to see a spirial graph？y/n:")
if answer == 'y':
   print("Drawing...")
   import turtle
   t = turtle.Pen()
   t.width(2)
   for x in range(100):
     t.forward(x*2)
     t.left(89)
print("Okay,the spirial graph you want to see has been drawn！")
