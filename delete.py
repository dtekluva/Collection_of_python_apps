##def list_printer(listn):
##    i=0
##    if type(listn) is list:
##        print()
##        print("PRINTING LIST !!!!")
##        print()
##        for item in listn:
##            print(i+1," : ",item)
##            print()
##            i+=1
##    if type(listn) is dict:
##        print()
##        print("PRINTING DICTIONARY !!!!")
##        print()
##        print ( listn.keys())
##        print()
##    else:
##        print()
##        print("PRINTING OTHER VALUES")
##        print()
##        print(listn)
##        print()
##   
##
##def triple_arg(arg1,arg2,arg3):
##    i=0
##    print("This is the triple arg function")
##    list_printer(arg1)
##    list_printer(arg2)
##    list_printer(arg3)
##    i+=1
##    
##
##
##
##
##listn=["boy","girl","woman",2,30000,"end",["meagre","solemn",2,3660,"again!!!"]]
##dicth={'Name': 'Zara', 'Age': 7,'Country':'Chad'}
##triple_arg(listn,dicth,45)


name=[]



def score_writer(name,score):
    ##print(name[0])
    high=open('save.txt','r')
    userhighs=high.readline().split()
    high.close()
    ##print(userhighs)
    file_write_holder=[]#main read holder
    player=[]#old fileread holder for split append

    for user in userhighs:
        player.append(user.split(':'))
    ##print(player)
    i=0
    for item in player:
        if int(player[i][1])<int(score):
            player[i][0]=name[0]
            player[i][1]=str(score)
            break
        i+=1    
        
    print(player)

    print(' \n {:<8}'.format('Nickname'),'    ','High score ')
    i=0
    for item in player:
        
        print('\n','{:*^8}'.format(player[i][0]),'    ',player[i][1])
        i+=1 
        
##first convert back to string 
    for item in player:
        file_write_holder.append(':'.join(item))

   ## print(file_write_holder)

    file = open('save.txt','w')

    file.write(' '.join(file_write_holder))##second convert back to string

    file.close()
    ##print(' '.join(file_write_holder))

    

name.append(input('Please enter a nickname : '))
score_writer(name,'200')


