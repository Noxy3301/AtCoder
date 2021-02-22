import math
n = int(input())
ans = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i*j > n:
            break
        ans += math.floor(n/(i*j))
print(ans)