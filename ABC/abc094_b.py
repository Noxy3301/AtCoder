n, m, x = map(int, input().split())
a = tuple(map(int, input().split()))
toZero = 0
toN = 0
for i in range(m):
    if a[i] < x:
        toZero += 1
    else:
        toN += 1
print(min(toZero,toN))