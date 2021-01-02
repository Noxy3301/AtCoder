n = int(input())
d = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n-1):
    for j in range(i+1, n):
        if d[i][0] != d[j][0]:
            if (d[j][1] - d[i][1])/(d[j][0] - d[i][0]) >= -1 and (d[j][1] - d[i][1])/(d[j][0] - d[i][0]) <= 1:
                ans += 1
print(ans)