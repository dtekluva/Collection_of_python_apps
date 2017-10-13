import random

dice_nums=[1,2,3,4,5,6]
troph1=[]
troph2=[]

player1=["name",0]
player2=["name",0]

player1[0]=input("Player 1 Please enter your name : ")
player2[0]=input("Player 2 Please enter your name : ")

def dice_roll():
    for i in range(4):
        dice1=random.choice(dice_nums)
        
    for i in range(4):
        dice2=random.choice(dice_nums)
        
    print(dice1,"     ", dice2)
    
    return dice1+dice2

for i in range(4):
    
    print(player1[0],", Please press enter to roll.  \n ")
    input("....")
    player1[1]= player1[1]+dice_roll()
    
    print(player2[0],", Please press enter to roll.  \n ")
    input("....")
    player2[1]= player2[1]+dice_roll()
    for i in range(player1[1]):
        troph1.append("0")
    
    for i in range(player2[1]):
        troph2.append("0")
        
    print(player1[0],"     ",  player1[1],"  Progress :  ",'{:-^100}'.format("".join(troph1)),"\n")
    print(player2[0],"     ",  player2[1],"  Progress :  ",'{:-^100}'.format("".join(troph2)),"\n")
#'\n','{:*^40}'.format("".join(troph2))
