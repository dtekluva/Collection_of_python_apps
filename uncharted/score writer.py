username=[]

def score_writer(name,score):
    global username
    high=open('save.txt','r')
    userhighs=high.readline().split()
    high.close()
    file_write_holder=[]#main read holder
    player=[]#old fileread holder for split append

    for user in userhighs:
        player.append(user.split(':'))
    i=0
    for item in player:
        if int(player[i][1])<int(score):
            player.insert(i,[9,0])
            player[i][0]=name
            player[i][1]=str(score)
            break
        i+=1

    while len(player)>5:
        player.remove(player[5])
    
    ##print(player)##first convert back to string 
    for item in player:
        file_write_holder.append(':'.join(item))

    file = open('save.txt','w')

    file.write(' '.join(file_write_holder))##second convert back to string

    file.close()

    player=[]#old fileread holder for split append

    for user in file_write_holder:
        player.append(user.split(':'))
    ##print(player)
    print(' \n\n{:<8}'.format('Nickname'),'    ','High scores ')
    i=0
    for item in player:##print all scores
        
        print('\n','{:*^8}'.format(player[i][0]),'    ',player[i][1])
        i+=1

##name.append(input('Please enter a nickname : '))
score_writer('username','1520')
