n = int(input())
h = tuple(map(int, input().split()))

dp = [0]

for i in range(1,n):
    if i == 1:
        dp.append(abs(h[i]-h[i-1]))
    else:
        dp.append(min(dp[-1]+abs(h[i]-h[i-1]), dp[-2]+abs(h[i]-h[i-2])))


print(dp[-1])