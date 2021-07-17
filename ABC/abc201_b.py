n = int(input())
d = []

for i in range(n):
    s,t = map(str, input().split())
    d.append([int(t),s])

d.sort()

print(d[-2][1])