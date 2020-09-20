def getdate():
    import datetime
    return datetime.datetime.now()


fstq = int(input("Press 1 for add data and 2 for view data : \n"))
secq = int(input("Press 1 for Mohit and 2 for Raj : \n"))
trdq = int(input("Press 1 for food press 2 for Exercise : \n"))
# For Add Data
if fstq == 1:
    # For Mohit
    if secq == 1:
        if trdq == 1:
            foodin = input("Please enter details : \n")
            with open("mohit_food.txt", "a") as mf:
                mf.write(str(getdate()))
                mf.write(" : ")
                mf.write(foodin)
                mf.write("\n")
        if trdq == 2:
            exerin = input("Please enter details : \n")
            with open("mohit_ex.txt", "a") as mf:
                mf.write(str(getdate()))
                mf.write(" : ")
                mf.write(exerin)
                mf.write("\n")
    # For Raj
    if secq == 2:
        if trdq == 1:
            foodin = input("Please enter details : \n")
            with open("raj_food.txt", "a") as mf:
                mf.write(str(getdate()))
                mf.write(" : ")
                mf.write(foodin)
                mf.write("\n")
        if trdq == 2:
            exerin = input("Please enter details : \n")
            with open("raj_ex.txt", "a") as mf:
                mf.write(str(getdate()))
                mf.write(" : ")
                mf.write(exerin)
                mf.write("\n")
# For View Data
if fstq == 2:
    # For Mohit
    if secq == 1:
        if trdq == 1:
            with open("mohit_food.txt", "r+") as mf:
                print(mf.read())
        if trdq == 2:
            with open("mohit_ex.txt", "r+") as mf:
                print(mf.read())
    # For Raj
    if secq == 2:
        if trdq == 1:
            with open("raj_food.txt", "r+") as mf:
                print(mf.read())
        if trdq == 2:
            with open("raj_ex.txt", "r+") as mf:
                print(mf.read())
"""

# Exercise 4 Gun, Water and Snake Game
"""
import random

aall = ["Gun", "Water", "Snake"]

randall = random.choice(aall)
total_avl_try = 5
total_try = 5
usrpoint = 0
compoint = 0
for i in range(5):
    randall = random.choice(aall)
    print(randall)
    usrrin = str(input("Please Choose Gun, Water OR Snake : \n"))
    usrin = usrrin.capitalize()
    i = i + 1
    if randall == "Gun":
        if usrin == "Water":
            print("You Earned 1 Point")
            usrpoint = usrpoint + 1
        elif usrin == "Snake":
            print("Computer Earned 1 Point")
            compoint = compoint + 1
        elif usrin == "Gun":
            print("Match Draw")
    elif randall == "Water":
        if usrin == "Snake":
            print("You Earned 1 Point")
            usrpoint = usrpoint + 1
        elif usrin == "Gun":
            print("Computer Earned 1 Point")
            compoint = compoint + 1
        elif usrin == "Water":
            print("Match Draw")
    elif randall == "Snake":
        if usrin == "Gun":
            print("You Earned 1 Point")
            usrpoint = usrpoint + 1
        elif usrin == "Water":
            print("Computer Earned 1 Point")
            compoint = compoint + 1
        else:
            print("Match Draw")
    else:
        compoint = compoint + 0
        usrpoint = usrpoint + 0
        print("Invailid Input")
    print("Your Point is : ", usrpoint)
    print("Computer Point Is : ", compoint)
    print("Total Try Left : ", (5 - i))
    
