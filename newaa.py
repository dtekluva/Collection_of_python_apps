################### WORD GUESS GAME ###############################

### import random is used when performing a random action
#### WORD_LIST is uppercase to show it is a constant
#### Note: return terminates execution
### def represents a function
import random

WORD_LIST = ["hello", "world", "class", "books", "table", "chairs", "pencil"]

def pick_word(list_word):
	word = random.choice(list_word)
	print("The word is", word)
	return word


def get_guess():
	print("Running an get_guess function")
	guess = input("Guess a word: ")   ### The user inputs in a word
	if not guess == "":               ### If the input is empty, it returns guess...user is asked to enter an input
		return guess 
	else:
		print("Words cannot be empty")
		get_guess()                     ###recursion takes place here....it repeats itself

### The user's input is compared with the word picked
def evaluate_guess(word, attempts):
	while attempts > 0:
		guess = get_guess()
		if guess != word:
			attempts -= 1
			print("Wrong attempt, you have ", attempts, "attempts left")
			evaluate_guess(word, attempts)
		else:
			print("Your guess is correct")
		break
	else:
		print("You have used up your attempts")
		return False
	return True
### Playing game
def play_game(game_count):
	game_count = 1
	word = pick_word(WORD_LIST)
	print("Welcome to the Word Guess Game")
	print()
	while evaluate_guess(word, 5):
		ask = input("Do you want to continue")
		if  ask == "y":
			game_count += 1
			play_game(game_count)		
		else:		
			print("You played ", game_count, "game")
			print("Goodbye")
			exit
	else:
		print("Oops you missed that one")
		retry =input("Do you want to try another word?")
		if  retry == "y":
			play_game(game_count)
		else:
			print("Goodbye")
			
play_game(0)
