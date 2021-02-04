n = int(input())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))

max_a, dekai = 0, 0
for i in range(n):
    max_a = max(max_a, a[i])
    dekai = max(dekai, max_a*b[i])
    print(dekai)