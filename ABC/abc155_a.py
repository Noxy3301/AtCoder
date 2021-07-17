d = tuple(map(int, input().split()))

st = set(d)

if len(st) == 2:
    print("Yes")
else:
    print("No")