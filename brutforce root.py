repeat =0


while repeat != 'EX' and repeat !='ex':

    inputval=int(input('please enter a value to test : '))
    test =0
    
    while (test*test*test*test*test) < inputval:
        test=test+1

        if test*test*test*test*test==abs(inputval):
            print (inputval ,' is a perfect 4th root ', test)

        elif test*test*test*test*test>abs(inputval):
            print (inputval, ' has no perfect 5th root value')
        else:
            x=1
            
    

    print ()

    repeat=input('please enter ex or EX to quit or another key to exit : ')
    print ()
    input()
