from banking_class import Banking

class BankingExpress(Banking):
    def in_transfer(self,sender,reciever,amount):
        if self.withdraw(sender,amount)==True:
            self.deposit(reciever,amount)

newaccount= BankingExpress("fidelity")
newaccount1= BankingExpress("fidelity")

print(newaccount.createAccount("inyang","08031346306","i@you.com"))
print(newaccount1.createAccount("paul","08031346306","i@you.com"))

newaccount1= BankingExpress("fidelity")
newaccount1.deposit(input("enter Accn"),int(input("enter Amount")))

newaccount.in_transfer(input("enter out Accn"),input("enter in Accn"),int(input("enter Amount")))
print(newaccount.balance)
