import math
ans = 0
N,D = map(int, input().split())
a = [list(map(int, input().split())) for i in range(N)]
for j in range(N):
  x = a[j][0] * a[j][0]
  y = a[j][1] * a[j][1]
  if math.sqrt(x + y) <= D:
    ans += 1
 
print(ans)