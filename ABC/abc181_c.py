import sys
n = int(input())
d = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if d[j][0] - d[i][0] == 0:
                grad = 0
            else:
                grad = (d[j][1] - d[i][1])/(d[j][0] - d[i][0])
            if grad*(d[k][0] - d[i][0]) + d[i][1] == d[k][1]:
                print("Yes")
                sys.exit()
print("No")