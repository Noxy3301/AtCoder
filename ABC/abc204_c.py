from collections import deque

n,m = map(int, input().split())
g = [[] for i in range(n)]

for i in range(m):
    a,b = map(int, input().split())
    g[a-1].append(b-1)

ans = 0
for i in range(n):
    move = [-1]*n
    move[i] = 1
    queue = deque()
    queue.append(i)

    while len(queue) != 0:
        v = queue.popleft()
        for j in g[v]:
            if move[j] == -1:
                move[j] = 1
                queue.append(j)
    ans += move.count(1)
print(ans)