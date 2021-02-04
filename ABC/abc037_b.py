n, q = map(int, input().split())
d = [0]*n
for i in range(q):
    l, r, t = map(int, input().split())
    for j in range(l,r+1):
        d[j-1] = t

for i in d:
    print(i)
