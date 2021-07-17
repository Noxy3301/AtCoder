n = int(input())
a = tuple(map(int, input().split()))
if len(a) == len(set(a)):
    print("YES")
else:
    print("NO")