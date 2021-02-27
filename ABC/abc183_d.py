n,w = map(int, input().split())
tl = []
isProvide = True
for i in range(n):
    s,t,p = map(int, input().split())
    tl.append([s,p])
    tl.append([t,-p])
tl.sort()

time = tl[0][0]
current = tl[0][1]
for i in range(1,len(tl)):
    if tl[i][0] != time:
        if current > w:
            isProvide = False
    time = tl[i][0]
    current += tl[i][1]

if isProvide:
    print("Yes")
else:
    print("No")