##cfile=open('save.txt','r')
##cspace=cfile.readline().split(" ")
##cfile.close()
##
##clist=[]
##for item in cspace:
##    clist.append(item.split(":"))
##    
##return clist
####print(clist)

####
newlist=[['alex', '08031346306', 'qwerty@yahoo.com', 'male', '3000000004', '680.0'],['alex', '08031346306', 'qwerty@yahoo.com', 'male', '3000000004', '680.0'],['jonah', '08022226106', 'qkoly@gmaoo.com', 'female', '3000000002', '680.0']]
##print(newlist)
##i=-1
##for item in newlist:
##    
##   newlist.append((':'.join(newlist.pop(i))))##second convert back to string
##   i-=1
##print(' '.join(newlist))


#print(space_join)
#colon_join=(':'.join(space_join))

##clist=[]
##for i in range(20000000):
##    clist.append(str(i))
##    
##print("newlist")
##
##for item in clist:
##    if item =="10000000":
##        print ("found 200000")

##    ##print(player)##first convert back to string
##file = open('sav.txt','w')
##
####space_join=(' '.join(clist))##second convert back to string
##file.writelines(clist)
##file.close()

##holder=[]
####print(player)##first convert back to string
##file = open('sav.txt','w')
##
##
##for item in newlist:
##    
##   holder.append((':'.join(item)))##second convert back to string
##   print(' '.join(holder))
##   
##file.close()

file = open('sav.txt','w')

use=str(file)
print(len(use))
#file.writelines(" ")

#file.writelines(':'.join(customer))##second convert back to string

file.close()



from fileio import fileio

banks=["Diamond","Fidelity","FirstBank"]
class Banking():
    balance=0.0
    
    def __init__(self,username,phone,email,gender,num_accs):
        self.username=username
        self.phone=phone
        self.email=email
        self.account=self.createAcc(num_accs)
        self.gender=gender      

    def createAcc(self,num_accns):
        global num_accs
        accountnumber=3000000001
        account=str(accountnumber+num_accns)
        
        return account

    def checkBalance(self,accn):
        return self.balance
    
    def deposit(self,amount):
        self.balance+=amount
        print(self.username," : you have deposited",amount,"and your balance is",self.balance,"\n\n")

    def withdraw(self,amount):
        if self.balance<amount:
            print("Insufficient funds")

        else:
            self.balance-=amount
            print(self.username," have withdrawn ",amount," and your balance is",self.balance,)
            return True
        
            

##cust_obj=Banking("frank ","08031346306","qwerty@yahoo.com","male")
##cust_obj2=Banking("James ","08031346306","qwerty@yahoo.com","male")
##cust_obj3=Banking("Affiong ","08031346306","qwerty@yahoo.com","female")
##account_no=cust_obj.createAcc(num_accs)
##print(cust_obj.username,"   :  ",cust_obj.checkBalance(account_no)," Acct no :   ",cust_obj.account, )
##cust_obj.withdraw(25000)
##
##cust_obj.deposit(500000)
##cust_obj.withdraw(1000)
##
##
##account_no=cust_obj2.createAcc(num_accs)
##print(cust_obj2.username,"   :  ",cust_obj2.checkBalance(account_no)," Acct no :   ",cust_obj2.account, )
##cust_obj2.withdraw(5000)
##cust_obj2.deposit(200000)
##cust_obj2.withdraw(1000)
##
##account_no=cust_obj3.createAcc(num_accs)
##print(cust_obj3.username,"   :  ",cust_obj3.checkBalance(account_no)," Acct no :   ",cust_obj3.account, )
##cust_obj3.withdraw(5000)
##cust_obj3.deposit(700000)
##cust_obj3.withdraw(102300)
##
##print(cust_obj.username,"   :  ",cust_obj.checkBalance(account_no)," Acct no :   ",cust_obj.account, )
##cust_obj.withdraw(25000)
##
##cust_obj.deposit(500000)
##cust_obj.withdraw(1000)
##
##
##print(cust_obj2.username,"   :  ",cust_obj2.checkBalance(account_no)," Acct no :   ",cust_obj2.account, )
##cust_obj2.withdraw(5000)
##cust_obj2.deposit(200000)
##cust_obj2.withdraw(1000)
##
##print(cust_obj3.username,"   :  ",cust_obj3.checkBalance(account_no)," Acct no :   ",cust_obj3.account, )
##cust_obj3.withdraw(5000)
##cust_obj3.deposit(700000)
##cust_obj3.withdraw(102300)

