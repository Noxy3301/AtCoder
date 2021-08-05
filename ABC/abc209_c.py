n = int(input())
c = list(map(int, input().split()))
c.sort()

dekai = 10**9+7
ans = 1

for i in range(n):
    ans *= max(0, c[i]-i) % dekai
    ans = ans%dekai
print(ans)