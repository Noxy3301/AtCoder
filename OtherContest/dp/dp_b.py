n,k = map(int, input().split())
h = tuple(map(int, input().split()))

dp = [0]

for i in range(1,n):
    tmp_min = 10**10
    for j in range(1,min(len(dp),k)+1):
        tmp_min = min(tmp_min, dp[-j]+abs(h[i]-h[i-j]))
    dp.append(tmp_min)
print(dp[-1])