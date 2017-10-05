word="0"

##def word_Reverser(rev_arg):

##    rev_word=[]
##    wordlist=[]
##    for item in word:
##        wordlist.append(item)
##    print ('  '.join(wordlist))
##    print()
##    i=-1
##    for item in word:
##        rev_word.append(word[i])
##        i-=1
##    
##    print (''.join(rev_word))
##    print()

    print("Reverse of the string is: ")
    print(rev_arg [::-1])     #(start:stop:count)string slicing -ve val make method count backward
    
while word!="exit":
    word=input("please enter a word to reverse:  ")
    word_Reverser(word)
