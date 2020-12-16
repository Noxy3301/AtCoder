x,y = map(int, input().split())
isComplete = False
for i in range(x + 1):
  if (2 * i) + (4 * (x-i)) == y:
    isComplete = True
 
if isComplete:
  print("Yes")
else:
  print("No")