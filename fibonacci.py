def fib(num):
    if(num<0):
        print('INCORRECT INPUT')
    elif(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return fib(num-1)+fib(num-2)

num=int(input('enter number of elements\n'))
print(fib(num))
