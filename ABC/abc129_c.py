n, m = map(int, input().split())
a = [int(input()) for i in range(m)]
mod = 10**9 + 7

if n <= 2:
    if n == 1 and m == 0:
        print(1)
    elif 1 in a[:2]:
        print(1)
    else:
        print(2)
else:
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 2
    if 1 in a[:2]:
        dp[2] = 1

    for i in range(m):
        dp[a[i]] = -1
    
    for i in range(3, n+1):
        if dp[i] != -1:
            if dp[i-1] == -1:
                if dp[i-2] == -1:
                    dp[i] = -1
                else:
                    dp[i] = dp[i-2]
            else:
                if dp[i-2] == -1:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
                    dp[i] %= mod

    if dp[-1] == -1:
        print(0)
    else:
        print(dp[-1])
