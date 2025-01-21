import random

rand=random.randint(1,100)

def higherorlower(choice):
    if rand > choice:
        print("go higher")
    elif rand < choice:
        print("go lower")
    elif rand == choice:
        print("you got it")

for i in range(10):
    user=int(input("give me a number i will tell you if it is close to my one" ))
    higherorlower(user)


    
 