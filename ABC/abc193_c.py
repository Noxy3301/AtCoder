def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i== 0:
            return False
    return True

import math
n = int(input())
d = []
for i in range(2, int(math.sqrt(n))+1):
    p = 2
    while pow(i,p) <= n:
        d.append(pow(i,p))
        p += 1
st = set(d)
print(n-len(st))