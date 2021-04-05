n = int(input())
a = tuple(map(int, input().split()))
d = [0]*n

for i in a:
    d[i-1] += 1

ans = 0
for i in range(n):
    if d[i] >= 2:
        ans += d[i]*(d[i]-1)//2

for i in range(n):
    if d[a[i]-1] > 1:
        print(ans - d[a[i]-1]+1)
    else:
        print(ans)