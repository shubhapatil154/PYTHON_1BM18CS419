def search(list,key):
    for i in list:
        if(i==key):
            print('KEY FOUND')
            break
    else:
       print('key not found')
       
    
list=[1,2,3,4,5,6,7]
key=int(input("enter the key element to be searched"))
search(list,key)
    
