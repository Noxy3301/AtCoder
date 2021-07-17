d = list(map(int, input().split()))
d.sort()

if d[2]-d[1] == d[1] - d[0]:
    print("Yes")
else:
    print("No")