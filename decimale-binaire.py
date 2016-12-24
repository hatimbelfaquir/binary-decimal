def Decimal(n):    
    a=0
    p=1
    while n!= 0:
        while (n-(2**p)) >= 0:
            p=p+1
        a=a+(10**(p-1))
        n=n-2**(p-1)
        p=0
    print(a)