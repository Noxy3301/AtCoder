#wa
def get_median(x,y,r):
    tmp = []
    for i in range(r):
        for j in range(r):
            tmp.append(d[x+i][y+j])
    tmp.sort(reverse=True)
    return tmp[(r**2)//2]


n,k = map(int, input().split())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))

ans = 10**18
for i in range(n-k+1):
    for j in range(n-k+1):
        aa = get_median(i,j,k)
        if ans > aa:
            ans = aa
print(ans)