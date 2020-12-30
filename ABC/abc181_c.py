import sys
n = int(input())
d = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            x1, y1 = d[i]
            x2, y2 = d[j]
            x3, y3 = d[k]
            x2 -= x1
            x3 -= x1
            y2 -= y1
            y3 -= y1
            if x3*y2 == x2*y3:
                print("Yes")
                sys.exit()
print("No")