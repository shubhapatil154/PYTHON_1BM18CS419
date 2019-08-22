def split_num(num_list):
    even_list = []
    for i in num_list:
        if( i % 2 == 0):
            even_list.append(i)
    print ('EVEN LIST IS:',even_list)
    
num_list=[]
n=input("enter the number of elements in the list\n")
for i in range(1,n):
    num_list.append(i)
split_num(num_list)



            
        
