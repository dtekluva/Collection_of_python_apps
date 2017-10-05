import string
import random



print("                                                 ;;    ")
print("                                                | |   ")
print("          ______________________________________|_|___")
print("         /____________________________________________\ ")
print("        /______________________________________________\ ")
print("        |----------------------------------------------|")
print("        |----WELCOME PLEASE ENJOY THE HANG MAN GAME----|")
print("        |--*NOTE THAT THE GAME IS NOT CASE SENSITIVE*--|")
print("        |----------------------------------------------|")
print("        |______________________________________________|")
print()
    

available=[]
word=["ANCIENT","AMMENDED","GRACE","THRONE","CONQUEST","NOBLE","ELEPHANT","ELEVATION"]
picked_word=random.choice(word)
game_count=0

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
    print()
    arg=input('please enter a letter  : ')
    print()
    
    while len(arg)!=1 :
        print()
        arg=input('Please enter not more or less than 1 letter  : ')
        print()
        
    return arg.upper()
        
     
def game_engine(word):
    score=0
    blank=[]
    blank2=[]
    tries=8
    print()
    print("|0_0|          THANK YOU, I HAVE PICKED AN",len(word),"LETTER WORD           |0_0|  ")
    print()
    print("|0_0|   YOU HAVE TO GUESS LETTER BY LETTER AND HAVE JUST .5.TRIES  |0_0|")
    print(word)
    ##list_conv("",word)
    print()
    list_conv(blank,available)    
    for item in word:
         blank.append("_")
         blank2.append("_")
    print ('  '.join(blank2))
         
    while tries>0:
        print()
        print("tries: " ,tries," <<<<<00000>>>>> Score " ,score)
        print()
        
        in_put=input_checker()
        i=0
        
        for item in word:
            j=0
            if in_put==word[i]:
                for item in available:
                    if in_put==available[j] :
                        score+=10
                        tries+=1
                        available[j]="_"
                    j+=1
                    
                blank[i]=word[i]
            i+=1
        tries-=1

        list_conv(blank,available)
        
        if "".join(blank)==word:
            print()
            print("Congrats, you won with ",8-tries,"fails")
            print()
            break
        if "".join(blank)!=word and tries==0:
            print()
            print("Sorry you have used up you tries!!!!")
            print()
            print("THE WORD WAS : ",word,"!!!")
            break

    return score*len(word)

        
                
def play_game(game_count):
    start=""
    score=0
    if game_count==0:
        start=input("|0_0|       Welcome, please press just the enter key to start      |0_0|")
        print()
       

    if len(start)==0:
        game_count+=1
        available_gen(game_count)
        score=game_engine(random.choice(word))
        
        print("|0_0| Do you want to try again (y/n) |0_0|")
        retry=input_checker()
        
        if retry=="Y":
            score=score*game_count
            play_game(game_count)
        else:
            score=score*game_count
            print("You played " ,game_count,"Games."," Total score |>>> ",score)      
            input("GOODBYE, COME BACK SOON")
    else:
        score=score*game_count
        input("GOODBYE, COME BACK SOON."," Total score |>>> ",score)

play_game(game_count)
