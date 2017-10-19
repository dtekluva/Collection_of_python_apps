customers=""

class fileio():

    def file_Reader():
        
        cfile=open('save.txt','r')
        cspace=cfile.readline().split(" ")
        cfile.close()

        clist=[]
        for item in cspace:
            clist.append(item.split(":"))
            
        return clist
        
    def cust_Writer(newlist):
        holder=[]
        ##print(player)##first convert back to string
        file = open('save.txt','w')
        
        for item in newlist:
    
           holder.append((':'.join(item)))##second convert back to string
           file.writelines(' '.join(holder))
           
        file.close()
        #print(customer)

    def cust_adder(name,phone,email,gender,accno,balance):
        customer=[name,phone,email,gender,accno,balance]
        ##print(player)##first convert back to string
        file = open('save.txt','a')

        use=str(file)
        if len(use)!=0:
            file.writelines(" ")
            
        file.writelines(':'.join(customer))##second convert back to string
        
        file.close()
        #print(customer)


        

##obj=fileio()
##obj.file_Reader()
        
##        for item in player:
##            file_write_holder.append(':'.join(item))
        

##        file = open('save.txt','w')
##
##        file.writeline(' '.join(file_write_holder))##second convert back to string
##
##        file.close()
##
##        player=[]#old fileread holder for split append
##
##        for user in file_write_holder:
##            player.append(user.split(':'))
##        ##print(player)
##        print(' \n\n{:<8}'.format('Nickname'),'    ','High scores ')
##        i=0
##        for num in range(5):##print all scores
##            
##            print('\n','{:*^8}'.format(player[i][0]),'    ',player[i][1])
##            i+=1


#file_Writer("name","phone","email","gender","accno")
