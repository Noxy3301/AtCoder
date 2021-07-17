n = int(input())
d = tuple(map(int, input().split()))

if len(set(d)) == n:
    print("Yes")
else:
    print("No")