def bubbleSort(nlist):
    for passnum in range(len(nlist)):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
                i+=1

nlist =  [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
bubbleSort(nlist)
print(nlist)
input()
