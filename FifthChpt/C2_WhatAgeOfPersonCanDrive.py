driving_age = eval(input("What age of people in your place can drive？"))
your_age = eval(input("Please input your name："))
if your_age >= driving_age:
    print("Congrats, you are old enough to drive！")
if your_age < driving_age:
    print("Sorry, you need",driving_age - your_age,"more years to drive.")
