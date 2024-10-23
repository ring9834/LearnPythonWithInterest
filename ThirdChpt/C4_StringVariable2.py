#打印多次输入的名字

name = input("Plese input your name")

for x in range(100):
    #在屏幕上显示100遍刚才输入的姓名
    print(name,end="Congrats！")
    # end=" "表示：每显示一次姓名，就在后面加上一个空格（代码用" "）
