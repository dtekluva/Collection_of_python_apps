max_attempts=5
WORD_LIST= ["name","car","plane","team","start"]

import random

def pick_word (listword):
    word=random.choice(listword)
    print("Hint: ", word)
    return word

def get_guess():
    guess= input("guess a word : ")
    if not guess=="":
        return guess

    else:
        print ("Guess cannot be empty")
        get_guess()


def evaluate_guess(attempts_left):
    

    if attempts_left!=max_attempts :
        word=word
    else:
        word=pick_word(WORD_LIST)
        guess=get_guess()
    if guess== word:
        return True
    else:
        return False

def play_game():
    if max_attempts==5:
        
        attempts_left=max_attempts
        attempts_left=attempts_left-1
    print(attempts_left)
    if evaluate_guess(max_attempts)==True:
        print("your guess is correct")
        resp=input("Do you want to try again (y/n) : ")

        if resp=="y":
            play_game()
        else:
            print("good bye")
    else:
        attempts_left-=1
        
        
play_game()
