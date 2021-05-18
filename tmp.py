n,m = map(int, input().split())
p = [[i] for i in range(n)]

for i in range(m):
    tmpA, tmpB = map(int, input().split())
    p[tmpA].append(tmpB)
    p[tmpB].append(tmpA)

ans = []
p_max = -1

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(i+2, n):
            tmp = set(p[i] + p[j] + p[k])
            if p_max < len(tmp):
                ans = []
                ans.append([i,j,k])
                p_max = len(tmp)
            elif p_max == len(tmp):
                ans.append([i,j,k])

for i in range(len(ans)):
    print(ans[i][0],ans[i][1],ans[i][2])