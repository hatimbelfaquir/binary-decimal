c=0
i=0
for i in range(1,1000):
    p = 0
    a = 0
    m = 0
    while i // 10**p != 0:
        a = int((i%(10**(p+1))-a)/(10**p))
        m = m + a**3
        p = p+1
    if m == i:
        print(i)