username=""
max_saves=5
userhighs=""
def file_Reader():
    global username
    global max_saves
    global userhighs
    high=open('save.txt','r')
    userhighs=high.readline().split()
    high.close()
    file_write_holder=[]#main read holder
    player=[]#old fileread holder for split append


def file_Writer(name,score):
    global username
    global max_saves
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
            player.insert(i,[0,0])
            player[i][0]=name
            player[i][1]=str(score)
            x=1
            break
        i+=1

    while len(player)>max_saves:
        player.remove(player[max_saves])
    
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
    for num in range(5):##print all scores
        
        print('\n','{:*^8}'.format(player[i][0]),'    ',player[i][1])
        i+=1

file_Writer("knbj",30450)
