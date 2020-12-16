N = int(input())
c = 0
flag = False
for i in range(N):
  x,y = map(int, input().split())
  if x == y:
    c += 1
    if c == 3:
      flag = True
  else:
    c = 0
 
if flag:
  print("Yes")
else:
  print("No")