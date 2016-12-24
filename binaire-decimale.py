def Binary(n):
    a=len(str(n))   #we have to calculate the number of characters in the nimber "n"
                    #but first of all we have to convert the number "n" into characters
    n=int(n)
    c=0
    p=0
    for c in range(0,a):
        if n%10==1:
            p=p+2**c
            n=(n-1)/10
        else:
            n=n/10
        c=c+1
    print(p)
