n,m = map(int, input().split())
h = tuple(map(int, input().split()))
g = [[] for i in range(n)]

for i in range(m):
    a,b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

ans = 0

for i in range(n):
    if len(g[i]) == 0:
        ans += 1
    else:
        flag = True
        for j in g[i]:
            if h[i] <= h[j]:
                flag = False
        if flag:
            ans += 1
print(ans)
