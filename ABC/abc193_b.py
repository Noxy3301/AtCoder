n = int(input())
ans = 10**10
for i in range(n):
    a,p,x = map(int, input().split())
    if a+1 <= x:
        ans = min(ans, p)
if ans == 10**10:
    print(-1)
else:
    print(ans)