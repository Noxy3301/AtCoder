from collections import deque

n,m = map(int, input().split())
g = [[] for i in range(n)]
mod = 10**9 + 7

for i in range(m):
    a,b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

dist = [-1]*n
dist[0] = 0

dp = [0]*n
dp[0] = 1

queue = deque()
queue.append(0)

while len(queue) != 0:
    v = queue.popleft()
    for i in g[v]:
        if dist[i] == -1:
            dist[i] = dist[v] + 1
            queue.append(i)
            dp[i] = dp[v]
        else: #探索済みであるけど最小経路である場合
            if dist[i] == dist[v] + 1:
                dp[i] += dp[v]

if dist[-1] == -1:
    print(0)
else:
    print(dp[-1]%mod)