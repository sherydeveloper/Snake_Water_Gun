# snake water gun Game

'''
snake = 1
water = -1
gun = 0
'''
import random
computer = random.choice([-1,0,1])

youstr = input("Enter Your Choice: ")
youDict = {
    "snake": 1,
    "water": -1,
    "gun": 0
}
you = youDict[youstr]
reverseDict = {
    1: "snake",
    -1:"water",
    0:"gun"
}

print(f"Computer's Choice is: {reverseDict[computer]} \n Your Choice is {reverseDict[you]}")

if(computer == you):
    print("It's a Draw!")
else:
    if(you == 1 and computer == -1):
        print("You Win!")
    elif(you == 0 and computer == -1):
        print("You Lose!")
    elif(you == -1 and computer == 1):
        print("You Lose!")
    elif(you == 0 and computer == 1):
        print("You Win!")
    elif(you == -1 and computer == 0):
        print("You Win!")
    elif(you == 1 and computer == 0):
        print("You Lose!")
    else:
        print("something went wrong!")
        
