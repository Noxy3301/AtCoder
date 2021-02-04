n,m = map(int, input().split())
a = tuple(map(int, input().split()))

n -= sum(a)

if n < 0:
    print(-1)
else:
    print(n)