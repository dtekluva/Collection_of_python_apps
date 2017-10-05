import string
import random



print("   |----------------------------------------------|")
print("   |----WELCOME PLEASE ENJOY THE HANG MAN GAME----|")
print("   |--*NOTE THAT THE GAME IS NOT CASE SENSITIVE*--|")
print("   |----------------------------------------------|")
print()
    

available=[]
word=["ANCIENT","AMMENDED","GRACE","THRONE","CONQUEST","NOBLE","ELEPHANT","ELEVATION"]
picked_word=random.choice(word)
game_count=1

def available_gen(game_count):
    
    i=0
    for item in string.ascii_uppercase:
        if game_count==1:
            available.append(string.ascii_uppercase[i])
        
        available[i]=string.ascii_uppercase[i]
        i+=1

def list_conv(arg1,arg2):

    print('  '.join(arg1))
    print(               )
    print('  '.join(arg2))
    

def input_checker():
    arg=input('please enter a letter  : ')
    
    while len(arg)!=1 :
            arg=input('Please enter not more or less than 1 letter  : ')
            print()
        
    return arg.upper()
        
     
def game_engine(word):
    blank=[]
    blank2=[]
    tries=3 
    list_conv("",word)
    print()
    list_conv(blank,available)    
    for item in word:
         blank.append("_")
         blank2.append("_")
    print ('  '.join(blank2))
         
    while tries>0:
        print("tries: " ,tries)
        print()
        in_put=input_checker()
        i=0
        tries
        for item in word:
            j=0
            if in_put==word[i]:
                for item in available:
                    if in_put==available[j] :
                        tries+=1
                        available[j]="_"
                    j+=1
                blank[i]=word[i]
            i+=1
        tries-=1
            
        list_conv(blank,available)

    return True

        
                
def play_game(game_count):
    
    start=input("|0_0| Welcome, please press just the enter key to start |0_0|")

    if len(start)==0:
        available_gen(game_count)
        game1=game_engine(random.choice(word))
        game_count+=1
        while game1==True:
            play_game(game_count)
    print("You played " ,game_count,"Games")      
    print("GOODBYE, COME BACK SOON")

play_game(game_count)
