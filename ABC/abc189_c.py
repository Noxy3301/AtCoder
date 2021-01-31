n = int(input())
a = tuple(map(int, input().split()))
ans = -1
for i in range(n):
    tiisai = a[i]
    for j in range(i,n):
        tiisai = min(tiisai, a[j])
        ans = max(ans, tiisai*(j-i+1))
print(ans)