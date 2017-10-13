num_accs=0
customer=[]
class Banking():
    balance=1000000.0
    
    def __init__(self,username,phone,email,gender):
        self.username=username
        self.phone=phone
        self.email=email
        self.account=Banking.createAcc(self,num_accs)
        self.gender=gender
        #Banking.custWriter(cust_obj.username,cust_obj.phone,cust_obj.email,cust_obj.account,cust_obj.gender)
        Banking.custWriter(self.username,self.phone,self.email,self.account,self.gender)
        

    def createAcc(self,num_accns):
        global num_accs
        accountnumber=3000000000
        self.account=str(accountnumber+num_accns)
        num_accs+=1
        
        
        

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
            print("You have withdrawn ",amount," and your balance is",self.balance,)
            return self.balance
        

    def custWriter(name,phone,email,gender,accno):
        details=[name,phone,email,gender,accno]
        customer.append(details)
        print(customer)
            

cust_obj=Banking("frank ","08031346306","qwerty@yahoo.com","male")

cust_obj2=Banking("James ","08031346306","qwerty@yahoo.com","male")
cust_obj3=Banking("Affiong ","08031346306","qwerty@yahoo.com","female")
account_no=cust_obj.createAcc(num_accs)
##print(cust_obj.username,"   :  ",cust_obj.checkBalance(account_no)," Acct no :   ",cust_obj.account, )
cust_obj.withdraw(25000)

cust_obj.deposit(500000)
cust_obj.withdraw(1000)


account_no=cust_obj2.createAcc(num_accs)
##print(cust_obj2.username,"   :  ",cust_obj2.checkBalance(account_no)," Acct no :   ",cust_obj2.account, )
cust_obj2.withdraw(5000)
cust_obj2.deposit(200000)
cust_obj2.withdraw(1000)

account_no=cust_obj3.createAcc(num_accs)
##print(cust_obj3.username,"   :  ",cust_obj3.checkBalance(account_no)," Acct no :   ",cust_obj3.account, )
cust_obj3.withdraw(5000)
cust_obj3.deposit(700000)
cust_obj3.withdraw(102300)

##print(cust_obj.username,"   :  ",cust_obj.checkBalance(account_no)," Acct no :   ",cust_obj.account, )
cust_obj.withdraw(25000)

cust_obj.deposit(500000)
cust_obj.withdraw(1000)


##print(cust_obj2.username,"   :  ",cust_obj2.checkBalance(account_no)," Acct no :   ",cust_obj2.account, )
cust_obj2.withdraw(5000)
cust_obj2.deposit(200000)
cust_obj2.withdraw(1000)

##print(cust_obj3.username,"   :  ",cust_obj3.checkBalance(account_no)," Acct no :   ",cust_obj3.account, )
cust_obj3.withdraw(5000)
cust_obj3.deposit(700000)
cust_obj3.withdraw(102300)
