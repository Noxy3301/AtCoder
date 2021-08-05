from collections import deque

#n個の頂点、m個の辺
n, m = map(int, input().split())
g = [[] for i in range(n)]

for i in range(m):
    a,b = map(int, input().split())
    g[b-1].append(a-1)
    g[a-1].append(b-1)

dist = [-1]*n   #開始した頂点からの距離を格納する
dist[0] = 0
queue = deque()
queue.append(0)

while len(queue) != 0:
    v = queue.popleft()
    for i in g[v]:
        if dist[i] != -1:   #頂点iが未探索(dist[i]が初期値の-1)でないなら
            continue
        dist[i] = dist[v] + 1
        queue.append(i)

print(dist)