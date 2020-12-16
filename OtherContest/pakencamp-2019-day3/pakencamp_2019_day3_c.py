N, M = map(int, input().split())
d = [list(map(int, input().split())) for i in range(N)]
ans = 0
for i in range(M-1):
    for j in range(i+1,M):
        temp = 0
        for k in range(N):
            temp += max(d[k][i],d[k][j])
        if temp > ans:
            ans = temp
print(ans)