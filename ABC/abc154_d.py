n,k = map(int, input().split())
p = tuple(map(int, input().split()))
exp = [(1+p[i])/2 for i in range(n)]
cum = [0]
tmp = 0
for i in range(n):
    tmp += exp[i]
    cum.append(tmp)

dekai = -1

for i in range(n-k+1):
    dekai = max(dekai, cum[i+k]-cum[i])

print(dekai)