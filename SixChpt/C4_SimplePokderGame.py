import random
suits = ["Club","Diamon","Heart","Spade"]
faces = ["two","three","four","five","six","seven","eight","nine","ten","jack","queen","king","ace"]
keep_going = True
while keep_going:
    my_face = random.choice(faces)
    your_face = random.choice(faces)
    my_suit = random.choice(suits)
    your_suit = random.choice(suits)
    print("I have",my_suit,",it's",my_face)
    print("You have",your_suit,",it's",your_face)
    if faces.index(my_face) > faces.index(your_face):
        print("I win！")
    elif faces.index(my_face) < faces.index(your_face):
        print("You win！")
    else:
        print("We are even！")
    answer = input("Press Enter to continue，any other keys to exit：")
    print(answer)
    keep_going = (answer == "")

