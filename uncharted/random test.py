##import random
##
##x=range(1,500,1)
##
##y=random.choice(x)
##print (y)

f = open("twist.txt","r") #opens file with name of "test.txt"

myList = []

for line in f:

    myList.append(line)

print(myList)
