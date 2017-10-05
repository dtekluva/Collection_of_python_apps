import math
#this program takes values as described by the pythagoras theorem for sides of a triangle and finds the length of a missing side
#user inputs zero(0) as the value for the unknown side

def hyp_C(adj_a,opp_b):
    '''calculates the hypotenus'''
    calc=float((opp_b**2)+(adj_a**2))
    hypothenus=float(math.sqrt(calc))
    return hypothenus

def adj_A(hyp_c,opp_b):
    '''calculates the adjacent'''
    calc=float((hyp_c*hyp_c))
    adjacent=float(math.sqrt(calc))
    return adjacent

def opp_B(hyp_c,adj_a):
    '''calculates the opposite'''
    calc=float((hyp_c*hyp_c)-(adj_a*adj_a))
    opposite=float(math.sqrt(calc))
    return opposite

def input_conv(inp_ut):
    while str.isdigit(inp_ut)!=True:
        inp_ut=input("invalid value please enter an integer : ")
        
    conv=int(inp_ut)
    return conv
              
        




retry=1
          
          
while (retry==1):

    print()
    print("________________________________________________")
    print("|----------------------------------------------|")
    print("|----WELCOME PLEASE ENJOY MATHS WITH PYTHON----|")
    print("|-------MAKE SURE TO INPUT REAL TRIANGLES------|")
    print("|----------------------------------------------|")
    print("|______________________________________________|")
    print()
    print()
    print("PLEASE ENTER THE VARIABLES OF YOUR TRIANGLE")
    print()
    print("ENTER ZERO (0) FOR THE UNKNOWN SIDE")
    print()
    print("E.G ADJACENT = 0 WOULD FIND THE ADJACENT")
    print("")
    
    adjacent=input("please enter adjacent: ")
    adj_int=input_conv(adjacent)
    
    opposite=input("please enter opposite: ")
    opp_int=input_conv(opposite)
    
    hypothenus=input("please enter hypothenus: ")
    hyp_int=input_conv(hypothenus)  #convert input value to float from str


    if adj_int==0:              #check if adjacent is the missing
       adj_result = adj_A(hyp_int,opp_int)
       print()
       print("The Adjacent of value for this triangle is: ", adj_result)
       print()
       adjacent=adj_result

    elif opp_int==0:            #check if opposite is the missing
        opp_result = opp_B(hyp_int,adj_int)
        print()
        print("The Opposite side of value for this triangle is: ", opp_result)
        print()
        opposite=opp_result

    elif hyp_int==0:            #check if hypothenus is the missing
        hyp_result = hyp_C(adj_int,opp_int)
        print()
        print("The Hypothenus of value for this triangle is: ", hyp_result)
        print()
        hypothenus=hyp_result

    else:
        print()
        print("SORRY NOTHING TO CALCULATE THERE WAS NO UNKNOWN VARIABLE")
        print()
        
    print("The sides of the triangle are: Adjacent",adjacent, ":: Opposite", opposite, ":: Hypothenus", hypothenus)

    print()
    retry=int(input("enter 1 to try again or any other key to exit : "))
