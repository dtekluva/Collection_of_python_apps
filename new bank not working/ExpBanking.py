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
        
    def accsearch(self,name,phone):
        i=0
        for item in custload:
            if name in item and phone in item:
                print("\n\n","-".join(item))
                break
            else:
                print("Sorry User not found")
                
        

custload= ExpBanking.file_Reader()
