def fib_guy(start,size):
    fib_list=[]
    
    for x in range(size):
        if x==0 or x==1:
            fib_list.append(start)
        else:
            fib_list.append(fib_list[x-1]+fib_list[x-2])
    return fib_list

print(fib_guy(int(input("\n please enter a Start int : ")),int(input("\n please enter an End int : "))))


  
