from collections import deque
n,m = map(int, input().split())
g = [[] for i in range(n)]

for i in range(m):
    a,b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

mark = [-1]*n
mark[0] = 0
query = deque()
query.append(0)

while len(query) != 0:
    v = query.popleft()
    for i in g[v]:
        if mark[i] != -1:
            continue
        mark[i] = v+1
        query.append(i)

if -1 in mark:
    print("No")
else:
    print("Yes")
    for i in range(1,n):
        print(mark[i])