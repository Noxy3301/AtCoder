n, m = map(int, input().split())
d = [0]*m
for i in range(n):
    hoge = tuple(map(int, input().split()))
    for j in range(hoge[0]):
        d[hoge[j+1]-1] += 1

ans = 0
for i in d:
    if i == n:
        ans += 1
print(ans)