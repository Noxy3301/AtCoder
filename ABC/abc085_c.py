n,y = map(int, input().split())
isComplete = False
 
for ichiman in range(n + 1):
  for gosen in range(n + 1):
    sen = (y - (ichiman*10000) - (gosen*5000)) // 1000
    zero = y - (ichiman*10000) - (gosen*5000) - (sen*1000)
    if zero == 0 and ichiman + gosen + sen == n and sen >= 0:
      print(str(ichiman) + " " +  str(gosen) + " " + str(sen))
      isComplete = True
      break
  if isComplete:
    break
 
if isComplete == False:
  print("-1 -1 -1")