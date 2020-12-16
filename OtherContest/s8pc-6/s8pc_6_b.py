n = int(input())
d = []
ans = 1000000000*30*30
for i in range(n):
    d.append(list(map(int, input().split())))

for i in range(len(d)):
    for j in range(len(d)):
        #print("i = {}, j = {}".format(i,j))
        temp = 0
        for k in range(len(d)):
            s = d[i][0]
            g = d[j][1]
            temp += abs(s-d[k][0]) + abs(d[k][0]-d[k][1]) + abs(d[k][1]-g)
            #print("temp = {}".format(temp))
        if ans > temp:
            ans = temp
print(ans)