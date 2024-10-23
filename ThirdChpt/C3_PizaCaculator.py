#比萨费用计算机器

#询问客户需要多少（几份）比萨，使用eval()求值
number_of_pizzas = eval(input("Please input how many boxes of pizza？"))

#每份比萨的价格。这里是固定价格15元，让变量cost_per_pizza记住这个值
cost_per_pizza = 15

#计算出所要的比萨需要多少钱
subtotal = number_of_pizzas * cost_per_pizza

#所需要的销售税额（即，销售税需要多少钱）
tax_tax = 0.08
sales_tax = subtotal * tax_tax

#加上销售税额后，这些比萨共需多少钱
total = subtotal + sales_tax

#向客户展示购买这些比萨，TA需要总共付多少钱
print("Hello，Your",number_of_pizzas,"boxes of pizza are worth in total",total,"dollars including",sales_tax,"dollars of selling tax，the tax rate is",tax_tax,"。")
