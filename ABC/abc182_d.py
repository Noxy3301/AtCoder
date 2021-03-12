#wa
n = int(input())
a = tuple(map(int, input().split()))
cum = [sum(a[:i+1]) for i in range(n)]
cum_l = [sum(cum[:i+1]) for i in range(n)]
cum_max = []
current = -10**9
for i in range(n):
    current = max(current, cum[i])
    cum_max.append(current)

dekai = -10**9
for i in range(n):
    dekai = max(dekai, cum_l[i]+cum_max[i])
print(max(dekai,0))