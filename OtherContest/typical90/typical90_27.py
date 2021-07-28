n = int(input())
dic = {}
name = []
for i in range(n):
    name.append(input())

for i in range(n):
    if name[i] not in dic:
        dic[name[i]] = i
        print(i+1)