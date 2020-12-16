a,b = map(int, input().split()) #a,bに[5 3]みたいな入力を格納できる
cost = sorted(map(int, input().split())) # 入力をソート
 
ans = 0
 
for i in range(0, b):
  ans = ans + cost[i]
 
print(ans)