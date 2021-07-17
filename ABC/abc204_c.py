n,m = map(int, input().split())
g = []

for i in range(n):
    g.append([])

for i in range(m):
    a,b = map(int, input().split())
    g[a-1].append(b-1)

ans = 0

for i in range(n):
    for j in range(n):
        if i == j:
            ans += 1
        else:
            flag = [0]*