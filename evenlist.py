def split_num(num_list):
    even_list = []
    for i in num_list:
        if( i % 2 == 0):
            even_list.append(i)
    print ('EVEN LIST IS:',even_list)
    
num_list=[]
n=input('enter the number of elements in the list\n')
print('enter the elemnts\n')
for i in range(0,n):
    elements=int(input())
    num_list.append(elements)
	
	
split_num(num_list)


            
        
