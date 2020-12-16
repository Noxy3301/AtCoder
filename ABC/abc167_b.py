a,b,c,k = map(int, input().split())
ans = 0
 
if k - a >= 0:
  ans = ans + a
  k = k - a
else:
  ans = ans + k
 
k = k - b
  
if k > 0:
  ans -= k
 
print(ans)