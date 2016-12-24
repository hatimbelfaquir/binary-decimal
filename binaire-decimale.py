def Binary(n):
    a=len(str(n))   #la valeur a calcule combien y a t-il de characters dans n
                    # Mais il faut convertir len n sous forme de chaîne de chartères
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