n = int(input())
d = tuple(input().split())
st = set(d)
if len(st) == 3:
    print("Three")
else:
    print("Four")