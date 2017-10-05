import random

WORD_LIST= ["name","car","plane","team","start"];

def pick_word(WORD_LIST):
    print ("running pick word")
    print ()
    word=random.choice(WORD_LIST)
    print("Hint: ", word)
    return word

def get_guess():
    guess= input("guess a word : ")
    if not guess=="":
        return guess

    else:
        print ("words cannot be empty")
        get_guess()

def evaluate_guess (word,attempts):
    
    while attempts > 0:
        guess = get_guess()
        if guess != word:
            attempts -=1
            print("wrong attepts, you have", attempts, "left")

            evaluate_guess(word,attempts)
        else:
            print("your guess is correct")
           
            
            break
    
    else:
        print("you have used up your attempt")
        
        return False
    return True

def play_game():
    game_count = 0
    word = pick_word(WORD_LIST)
    print("welcome to word guess game")
    print()
    while evaluate_guess(word,5):
        ask = input("do you want to continue")
        if ask == "Y":
            game_count +=1
            play_game()
        else:
            print("you played", game_count, "game")
            print("goodbye")
    else:
        print("oops you missed that one")
        retry = input("do you want to try another word(y/n) : ")
        if retry == "y":
            play_game()
        else:
            print("goodbye")


play_game()
