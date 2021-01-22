n = int(input())
d = list(map(int, input().split()))
while len(d) >= 2:
    d.sort()
    d.append((d[0]+d[1])/2)
    d = d[2:]
print(d[0])