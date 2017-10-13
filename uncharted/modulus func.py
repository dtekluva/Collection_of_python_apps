def string_mod(str_in):
    mod_holder=[]
    for x in range(len(str_in)):
        if x==0:
            mod_holder.append("non mod")
        else:
            mod_holder.append(len(str_in)%(x))
   
    return mod_holder

print(string_mod(input("please enter a string : ")))
