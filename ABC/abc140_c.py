n = int(input())
d = list(map(int, input().split()))

for i in range(1,n-2):
    if d[i-1] < d[i] and d[i] > d[i+1]:
        d[i] = max(d[i-1], d[i+1])
    elif d[i-1] > d[i] and d[i] < d[i+1]:
        d[i] = min(d[i-1], d[i+1])

print(d)