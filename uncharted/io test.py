import random
import string
f = open("twist.txt","r") #opens file with name of "test.txt"

me=f.readline()
print ("Loading word list from file...")
me = str.split(me)
men=len(me)
me=random.choice(me)
##print(f.read(55))
print (me)
print (men)

f.close()
##print ("Loading word list from file...")
### inFile: file
##inFile = open("twist.txt", 'r')
### line: string
##line = inFile.readline()
### wordlist: list of strings
##wordlist = str.split(line)
###print(line)
##
##
##print ("  ", len(wordlist), "words loaded.")


