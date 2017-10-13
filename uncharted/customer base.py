username=[]
global cust_list
cust_list=[]#old fileread holder for split append
def score_reader(name,score):
    global username
    high=open('customers.txt','r')
    customers=high.readline().split()
    high.close()
     
    
    for user in customers:
        cust_list.append(user.split(':'))
    i=0
   
    print (cust_list)
    score_writer(1,1,1,1,1)
    
   
def score_writer(name,acc,bal,sex,age):
    
    new_values=[str(name),str(acc),str(bal),str(sex),str(age)]
    cust_list.append(new_values)
    ##first convert back to string
    file_write_holder=[]#main read holder
    print (cust_list)
    for item in cust_list:
        file_write_holder.append(':'.join(item))

    file = open('customers.txt','w')

    file.write(' '.join(file_write_holder))##second convert back to string

    file.close()

    customer=[]#new fileread holder for split append

    for user in file_write_holder:
        customer.append(user.split(':'))
    
    print(' \n\n{:<8}'.format('Nickname'),'    ','High scores ')
    i=0
    for item in customer:##print all scores
        
        print('\n','{:*^8}'.format(customer[i][0]),'    ',customer[i][1],customer[i][2],customer[i][3],customer[i][4])
        i+=1

##name.append(input('Please enter a nickname : '))
score_reader('username','0')
