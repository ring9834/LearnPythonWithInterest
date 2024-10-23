import random
the_number =  random.randint(1,10)
guess = int(input("Please input a number between 1 and 10："))
while guess != the_number:
    if guess > the_number:
        print("What you guess is ",guess,"bigger")
    if guess < the_number:
        print("What you guess is",guess,"smaller")
    guess = int(input("Please guess another number："))
print("Congrats, you are right！")
