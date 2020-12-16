N = int(input())
d = list(map(int, input().split()))
min = 0
ans = 0
for i in d:
  if i > min:
    min = i
  else:
    ans += min - i
 
print(ans)