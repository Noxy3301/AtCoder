n = int(input())
a = tuple(map(int, input().split()))
d = [0]*n

for i in range(n-1):
    d[a[i]-1] += 1
for i in d:
    print(i)