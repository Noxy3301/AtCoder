n,k = map(int, input().split())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))

ans = 0
for i in range(n):
    ans += abs(a[i]-b[i])

if ans > k:
    print("No")
else:
    if (ans-k)%2 == 0:
        print("Yes")
    else:
        print("No")