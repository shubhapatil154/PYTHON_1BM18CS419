def divisors(num):
    print(f'DIVISORS OF THE NUMBER {num} is')
    for  i in range(1,num+1):
        if(num%i==0):
            print(i)


num=int(input('ENTER THE NUMBER \n'))
divisors(num)
