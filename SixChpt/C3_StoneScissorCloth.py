import random
choices = ["Stone","Cloth","Scissor"]
print("Game Rule：Stone can break Scissor, Scissor can break Cloth, and Cloth can cover Stone.")
player = input("Pleae input your selection, Stone, Scissor, Or Cloth? or input 9 to exit：")
while player != "9":
    player = player.lower()
    computer =random.choice(choices)
    print("Yours is",player,",Computer's is",computer,"。")
    if player == computer:
        print("Your are even with Computer！")
    elif player == "Stone":
        if computer == "Scissor":
            print("Congrats, you win over Computer！")
        else:
            print("Sorry, Computer win！")
    elif player == "Scissor":
        if computer == "Cloth":
            print("Congrats, you win over Computer！")
        else:
            print("Sorry, Computer win！")
    
    elif player == "Cloth":
        if computer == "Stone":
            print("Congrats, you win over Computer！")
        else:
            print("Sorry, Computer win！")
    else:
        print("There is something wrong with the game.")

    print()    
    player = input("Pleae input your selection, Stone, Scissor, Or Cloth? or input 9 to exit：")
