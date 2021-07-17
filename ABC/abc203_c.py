import sys
n, k = map(int, input().split())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))

d = sorted(d, key=lambda x:x[0])

current = 0

for i in d:
    if k - (i[0] - current) < 0:
        print(current + k)
        sys.exit()
    else:
        k += i[1] - (i[0] - current)
        current = i[0]

print(current + k)