from Banking import Banking
from fileio import fileio

custload=[]
activecust=["",""]

class ExpBanking(Banking,fileio):
     
    def transfer(self,reciever,amount):
        if self.withdraw(amount)==True:
            reciever.deposit(amount)


    def userLoader(self,accno):
        
        i=0
        for item in custload:
            
            if accno in item :
                
                item=custload.pop(i)
                
                self.username=item[0]
                self.phone=item[1]
                self.email=item[2]
                self.gender=item[3]
                self.account=item[4]
                self.balance=float(item[5])
                
            i+=1
        
        ExpBanking.cust_Writer(custload)
        


##def main():
##    global custload
##    custload= ExpBanking.file_Reader()
##    activecust[0]=ExpBanking("","","","",0)
##    activecust[1]=ExpBanking("","","","",0)
##    print("\n\n llooaad:    \n\n",custload,"\n\n")
##
##    newAccount=ExpBanking("Affiong ","08031346306","qwerty@yahoo.com","female",int(len(custload)-1))
##
##
##    print("wooooooow",custload)
##    activecust[0].userLoader("3000000001")
##    activecust[1].userLoader("3000000002")
##    activecust[0].deposit(50)
##    activecust[0].transfer(activecust[1],300)
##
##    print(activecust[0].username,"   :  ",activecust[0].checkBalance(activecust[1].account)," Acct no :   ",activecust[0].account)
##    print(activecust[1].username,"   :  ",activecust[1].checkBalance(activecust[1].account)," Acct no :   ",activecust[1].account)
##    print(newAccount.username,"   :  ",newAccount.checkBalance(newAccount.account)," Acct no :   ",newAccount.account)
##
##
##    ExpBanking.cust_adder(activecust[0].username,activecust[0].phone,activecust[0].email,activecust[0].gender,activecust[0].account,str(activecust[0].balance))
##    ExpBanking.cust_adder(activecust[1].username,activecust[1].phone,activecust[1].email,activecust[1].gender,activecust[1].account,str(activecust[1].balance))
##
###main()


###activecust[0]=ExpBanking("frank ","08031346306","qwerty@yahoo.com","male")
custload= ExpBanking.file_Reader()
##activecust[0]=ExpBanking("","","","",0)
##activecust[1]=ExpBanking("","","","",0)
##print("\n\n llooaad:    \n\n",custload,"\n\n")
##
##newAccount=ExpBanking("Affiong ","08031346306","qwerty@yahoo.com","female",int(len(custload)-1))
##
##
##print("custload",custload)
##activecust[0].userLoader("3000000001")
##activecust[1].userLoader("3000000002")
##activecust[0].deposit(50)
##activecust[0].transfer(activecust[1],300)
##
##print(activecust[0].username,"   :  ",activecust[0].checkBalance(activecust[1].account)," Acct no :   ",activecust[0].account)
##print(activecust[1].username,"   :  ",activecust[1].checkBalance(activecust[1].account)," Acct no :   ",activecust[1].account)
##print(newAccount.username,"   :  ",newAccount.checkBalance(newAccount.account)," Acct no :   ",newAccount.account)
##
##
##ExpBanking.cust_adder(activecust[0].username,activecust[0].phone,activecust[0].email,activecust[0].gender,activecust[0].account,str(activecust[0].balance))
##ExpBanking.cust_adder(activecust[1].username,activecust[1].phone,activecust[1].email,activecust[1].gender,activecust[1].account,str(activecust[1].balance))
##
