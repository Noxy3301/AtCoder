n = int(input())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))

ans = 0

for i in range(n):
    ans += a[i]*b[i]

if ans == 0:
    print("Yes")
else:
    print("No")