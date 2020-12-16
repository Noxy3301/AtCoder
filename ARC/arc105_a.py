d = list(map(int, input().split()))
goukei = sum(d)
ans = 0
flag = False
for i in range(2**len(d)):
  temp = 0
#  print("-"*20)
  for j in range(len(d)):
    if ((int(bin(i)[2:]) >> j) & 1):
#      print("{}|食べるクッキーは{}".format((int(bin(i)[2:])),j))
      temp += d[j]
#  print("goukei-temp={}/temp={}".format(goukei-temp,temp))
  if goukei - temp == temp:
    flag = True
 
if flag:
  print("Yes")
else:
  print("No")