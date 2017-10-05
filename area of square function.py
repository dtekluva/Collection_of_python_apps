def squareArea(length,breadth):
    '''this function evaluates the  area of a square '''
    area=length*breadth
    
    return area
   

length=int(input("please enter length: "))
breadth=int(input("please enter breadth: "))

print("The Area of the square with sides ",length,"cm", "and", breadth, "is : ", squareArea(length,breadth))
