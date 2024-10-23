import random
keep_going = True
while keep_going:
    dice = [0,0,0,0,0]
    for i in range(5):
        dice[i] = random.randint(1,6)
    print("What you throw is：",dice)
    dice.sort()

    if dice[0] == dice[4]:
        print("Yahtree！straight flush！")
    elif (dice[0] == dice[3] or dice[1] == dice[4]):
        print("The four are the same！")
    elif (dice[0] == dice[2] or dice[1] == dice[3] or dice[2] == dice[4]):
        print("The three are the same！")
    answer = input("Press Enter to continue，any other keys to exit：")
    keep_going = (answer == "")
