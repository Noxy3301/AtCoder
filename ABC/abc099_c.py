n = int(input())
dp = [0]

for i in range(1,n+1):
    tmp_pow6 = 0
    tmp_pow9 = 0
    while i - 6**(tmp_pow6+1) >= 0:
        tmp_pow6 += 1
    while i - 9**(tmp_pow9+1) >= 0:
        tmp_pow9 += 1
    tmp_min = min(dp[-1]+1, dp[-(6**tmp_pow6)]+1, dp[-(9**tmp_pow9)]+1)
    dp.append(tmp_min)
print(dp[-1])