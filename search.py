def search(list,key):
    for i in list:
        if(i==key):
            return True
            break
    else:
       return  False
       
    
list=[1,2,3,4,5,6,7]
key=int(input("enter the key element to be searched"))
result=search(list,key)
if(result==True):
    print('KEY FOUND')
else:
    print('key not found')
