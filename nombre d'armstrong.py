n = int(input())
p = 0
a = 0
m = 0
while n // 10**p != 0:
    a = int((n%(10**(p+1))-a)/(10**p))
    m = m + a**3
    p = p+1
if m == n:
    print(n,"est un nombre d'Armstrong.")
else:
    print(n,"n'est pas un nombre d'Armstrong.")