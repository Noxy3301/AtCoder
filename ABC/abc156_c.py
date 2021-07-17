n = int(input())
x = tuple(map(int, input().split()))

ans = 10**10

for i in range(0,101):
    tmp = 0
    for j in range(n):
        tmp += (x[j]-i)**2
    ans = min(ans , tmp)

print(ans)