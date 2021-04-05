n,m = map(int, input().split())
d = tuple(map(int, input().split()))
goukei = sum(d)
ans = 0

for i in range(n):
    if d[i] >= goukei/(4*m):
        ans += 1

if ans >= m:
    print("Yes")
else:
    print("No")