import sys
n, x = map(int, input().split())
hoge = 0
for i in range(n):
    v, p = map(int, input().split())
    hoge += v*p
    if hoge > x*100:
        print(i+1)
        sys.exit()
print(-1)