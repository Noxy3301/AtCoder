import sys

n,m = map(int, input().split())
g = []
for i in range(m):
    g.append([])
print(g)

for i in range(m):
    a,b = map(int, input().split())
    g[a-1].append(b)
    g[b-1].append(a)
    print(g)

for i in range(m): #1頂点から3本以上の辺が生えてたら無理
    if len(g[b-1]) >= 3 or len(g[a-1]) >= 3:
        print(0)
        sys.exit()

flag = [0]*m
ans = 1

for i in range(n):
    queue = []
    if flag[0] == 0:
        flag = 1
    if queue == []:
        ans *= 3
    else:
        queue = g[i]
        while len(queue) != 0:
            if flag[queue[0]] == 0:
                flag[queue[0]] = 1
                



#わかんね～～～～～～～～～～～～
