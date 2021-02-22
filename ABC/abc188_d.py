n,x = map(int, input().split())
tl = []
ans = 0
for i in range(n):
    a,b,c = map(int, input().split())
    tl.append([a-1,c])
    tl.append([b,-c])
tl.sort()

prev = tl[0][0]
current = tl[0][1]
for i in range(1,len(tl)):
    if tl[i][0] != prev:
        ans += (tl[i][0]-prev)*min(x,current)
    current += tl[i][1]
    prev = tl[i][0]
print(ans)