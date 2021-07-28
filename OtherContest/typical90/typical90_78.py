n,m = map(int, input().split())
vertex = [0]*n

for i in range(m):
    d = list(map(int, input().split()))
    d.sort()
    vertex[d[-1]-1] += 1

ans = 0
for i in vertex:
    if i == 1:
        ans += 1
print(ans)