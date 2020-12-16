D,T,S = map(int, input().split())
ts = T*S
if ts - D >= 0:
  print("Yes")
else:
  print("No")