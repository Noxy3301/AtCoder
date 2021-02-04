n, k = map(int, input().split())
d = [0]*k
while n != 0:
    for i in range(k):
        if n == 0:
            break
        d[i-1] += 1
        n -= 1
print(max(d)-min(d))