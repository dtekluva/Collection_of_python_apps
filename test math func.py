import math

def hyp_C(adj_A,opp_B):
    calc=float((opp_B*opp_B)+(adj_A*adj_A))
    hypothenus=math.sqrt(calc)
    return hypothenus


a=int(input("input a :"))
b=int(input("input b :"))
summ=hyp_C(a,b)
print(summ)
k
