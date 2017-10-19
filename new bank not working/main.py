from ExpBanking import ExpBanking
from Banking import Banking
from fileio import fileio

custload=[]
activecust=["",""]

def deposit(accno,amount):
    custload= ExpBanking.file_Reader()
    activecust[0]=ExpBanking("","","","",0)
    activecust[0].userLoader(accno)
    activecust[0].deposit(amount)
    print(activecust[0].balance)
    ExpBanking.cust_adder(activecust[0].username,activecust[0].phone,activecust[0].email,activecust[0].gender,activecust[0].account,str(activecust[0].balance))
  
def userIn(display):
    print("Please enter ",display," :>> ")

    return (input()).upper()
    
def withdraw(accno,amount):
    custload= ExpBanking.file_Reader()
    activecust[0]=ExpBanking("","","","",0)
    activecust[0].userLoader(accno)
    print(activecust[0].balance)
    activecust[0].withdraw(amount)
    ExpBanking.cust_adder(activecust[0].username,activecust[0].phone,activecust[0].email,activecust[0].gender,activecust[0].account,str(activecust[0].balance))
  

def newuser(name,phone,email,gender,):
    custload= ExpBanking.file_Reader()
    newAccount=ExpBanking(name,phone,email,gender,int(len(custload)-1))
    ExpBanking.cust_adder(newAccount.username,newAccount.phone,newAccount.email,newAccount.gender,newAccount.account,str(newAccount.balance))

def accsearch(name,phone):
    custload= ExpBanking.file_Reader()
    i=0
    for item in custload:
        if name in item and phone in item:
            print("\n\n","-".join(item))
            i+=1
            break
    if i==0:
        print("Sorry User not found")

def transfer(outAcc,inAcc,amount):
    custload= ExpBanking.file_Reader()
    activecust[0]=ExpBanking("","","","",0)
    activecust[1]=ExpBanking("","","","",0)
    activecust[0].userLoader(outAcc)
    activecust[1].userLoader(inAcc)
    activecust[0].transfer(activecust[1],amount)
    ExpBanking.cust_adder(activecust[0].username,activecust[0].phone,activecust[0].email,activecust[0].gender,activecust[0].account,str(activecust[0].balance))
    ExpBanking.cust_adder(activecust[1].username,activecust[1].phone,activecust[1].email,activecust[1].gender,activecust[1].account,str(activecust[1].balance))
    
def bankEngine():
    
    key=""
    while key not in ["D","T","W","S","N"]:
        print("D to Deposit, T to Transfer, W to Withdraw or S to Search for ACC, or N to Create Acc \n\n")
        key=(input("Please What do you want to do : ")).upper()
        if key=="D":
            deposit(userIn("Acc No "),float(userIn("Amount ")))
            break
        if key=="T":
            transfer(userIn("source accNo "),userIn("reciever accNo "),float(userIn("Amount ")))
            break
        if key=="W":
            withdraw(userIn("Acc No "),float(userIn("Amount ")))
            break
        if key=="S":
            accsearch(userIn("Name"),userIn("Phone number"))
            break
        if key=="N":
            newuser(userIn("Name"),userIn("Phone "),userIn("Email"),userIn("Gender"))
            print("\n\nCreated")
            break
        else:
            print("invalid input")
        
bankEngine()
