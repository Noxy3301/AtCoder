w,h = map(int, input().split())
mod = 10**9 + 7

"""
dp
"""
dp = []

dp.append([1]*w)
for i in range(1,h):
    dp.append([1] + [0]*(w-1))

for i in range(1,h):
    for j in range(1,w):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])%mod

print(dp[h-1][w-1])

"""
combination
"""
# import math
# w -= 1
# h -= 1
# print(math.factorial(w+h)//(math.factorial(w)*math.factorial(h)) % mod)