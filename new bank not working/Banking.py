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
