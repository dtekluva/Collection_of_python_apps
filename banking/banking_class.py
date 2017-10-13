import random

class Banking():
    balance=0
    def __init__(self,bankname):
        self.bankname=bankname
    def generate_accn(self,prefix,lenght):
        acn=""
        for x in range(lenght-2):
            acn+=str(random.randrange(9))

        acn=str(prefix)+acn
        return acn
    
    def createAccount(self,name,phone,email):
        acn=self.generate_accn(self.bankname[:2],10)
        acc_dict={"name":name,"phone":phone,"email":email,"accn":acn}
        newfile=open("acct_rec.txt",'w')
        newfile.writelines(str(acc_dict))
        newfile.close()
        return acc_dict

    def deposit(self,accn,amount):
        #retrieve records
    
        acct_rec=open("acct_rec.txt",'r')
        records=acct_rec.readline()
        print(records)
        self.balance=amount+self.balance
           

    def withdraw(self,accn,amount):
        
        if self.balance<amount:
            print("insufficient balance")
            return False
        else:
            self.balance-=amount
            print("you have withdrawn ",amount," and your new balance is ",self.balance)
            return True

##newaccount= Banking("DIAMOND")
##print(newaccount.createAccount("inyang","08031346306","i@you.com") )             
##        
##newaccount.deposit("jnvksd",3000)
##print(newaccount.balance)
