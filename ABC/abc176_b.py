N = int(input())
strN = str(N)
wa = 0
for i in strN:
  wa += int(i)
 
if wa % 9 == 0:
  print("Yes")
else:
  print("No")