n, m, c = map(int, input().split())
b = tuple(map(int, input().split()))
ans = 0

for i in range(n):
    a = tuple(map(int, input().split()))
    hoge = sum([a[j]*b[j] for j in range(m)]) + c
    if hoge > 0:
        ans += 1
print(ans)