import random
WORD_LIST= ["name","car","plane","team","start"];
attempts=5

def pick_word():
    print ("running pick word")
    print ()
    word=random.choice(WORD_LIST)
    print("Hint: ", word)
    return word

def get_guess():
    print ("running get_guess")
    print ()
    guess= input("guess a word : ")
    if not guess=="":
        return guess

    else:
        print ("Guess cannot be empty")
        get_guess()

def evaluate_guess(attempts):
    print ("running evaluate_guess")
    print ()
    picked=pick_word()
    guess=get_guess()
       
    while picked!=guess and attempts>=1:
        print(attempts, picked)
        print("Please try again : ")
        guess=get_guess()
        attempts=attempts-1
        
    if picked==guess:
        print("WELDONE YOU ARE A SMART MAN ")
    

def main_game():
    print ("running main_game")
    print ()
    evaluate_guess(attempts)
    retry=input("Do you want to try again (y/n : ")
   
    if retry == "y":
        main_game()
    else:
        print("BYE ")


main_game()
   
