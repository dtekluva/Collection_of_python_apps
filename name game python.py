import random

possible_options=['one','two','three','four','five','six','seven']


picked_value = random.choice(possible_options)

def guessing_game(picked_value,possible_options): 
    '''this code picks a random values from a list and asks the user to guess, while also counting the number of tries used by the user'''
    
    print('HERES YOUR GUESS LIST : ', possible_options)
    tries= 1
    
    print()
    guess=input('Please guess a text from the options : ') 
    print()
    
    while picked_value!=guess:  
        tries=tries+1        
        print('wrong value, please try again : ')
        print()
        guess=input('Please guess a text from the options : ')
            

    print('Viola you are a genius monsieur  (',tries  ,' ) : tries')
    print()
    


guessing_game(picked_value,possible_options) 
    
