n = int(input())
data = list(map(int, input().split()))
data.sort()
data.reverse()
 
while data[-1] == 0:
  data.insert(0,0)
  data.pop(-1)
 
ans = 1
 
for d in data:
  ans = ans * int(d)
  if ans > 10**18 or ans == 0:
    break
 
if ans > 10**18:
  print(-1)
else:
  print(ans)