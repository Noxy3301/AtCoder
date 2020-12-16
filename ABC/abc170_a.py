data = list(map(int, input().split()))
num = 1
 
for i in data:
    if num != i:
      print(num)
    num += 1