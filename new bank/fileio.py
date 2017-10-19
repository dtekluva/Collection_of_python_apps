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
        file = open('save.txt','w')
        
        for item in newlist:
    
           holder.append((':'.join(item)))##second convert back to string
        file.writelines(' '.join(holder))  
        file.close()

    def cust_adder(name,phone,email,gender,accno,balance):
        customer=[name,phone,email,gender,accno,balance]
        file = open('save.txt','a')

        use=str(file)
        if len(use)!=0:
            file.writelines(" ")
            
        file.writelines(':'.join(customer))##second convert back to string
        
        file.close()
