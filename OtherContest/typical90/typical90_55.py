import itertools
n,p,q = map(int, input().split())
a = list(map(int,input().split()))
remainder = []

for i in range(n):
    remainder.append(a[i]%p)

comb = itertools.combinations(remainder,5)
ans = 0

for i in comb:
    if i[0]*i[1]%p*i[2]%p*i[3]%p*i[4]%p == q:
        ans += 1
print(ans)