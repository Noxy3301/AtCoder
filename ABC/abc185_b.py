n, m, t = map(int, input().split())
max_n = n
d = [tuple(map(int, input().split())) for _ in range(m)]
flag = 1
 
time = 0
for i in range(m):
    n -= d[i][0]-time
    if n <= 0:
        flag = 0
    time = d[i][0]
    n = min(max_n,n+d[i][1]-time)
    time = d[i][1]
 
n -= t-time
if n <= 0:
    flag = 0
 
if flag == 0:
    print("No")
else:
    print("Yes")