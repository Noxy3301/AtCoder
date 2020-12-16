x = int(input())
d = list(map(int, input().split()))
count = 0
for i in range(len(d)):
  for j in range(i+1,len(d)):
    for k in range(j+1,len(d)):
      temp = []
      temp.extend([d[i],d[j],d[k]])
      temp.sort()
      if temp[0] + temp[1] > temp[2] and len(list(set(temp))) == 3:
        count += 1
print(count)