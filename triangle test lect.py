def findSide(side_unknown,knownsideA,knownsideB):
    '''hyp,or adj,or ,opp'''
    
    
    sideslist=["hyp","adj","opp"]
    if side_unknown in sideslist:
        if side_unknown=='hyp':
           
            result=((knownsideA**2)+(knownsideB**2)**0.5)
        elif side_unknown=='adj':
            result=((knownsideA**2)-(knownsideB**2)**0.5)
        else:
            result=((knownsideA**2)-(knownsideB**2)**0.5)
    
    else:
        print("INPUT ERROR")
    return result

unknown=input("please enter hyp,or adj,or ,opp for missing side : ")
first_side=int(input("please enter value for side 1 : "))
second_side=int(input("please enter value for side 2 : "))
result = findSide(unknown,first_side,second_side)
print("the result is : ",result)
input()
