n = int(input())
dame = [int(input()) for i in range(3)]

if n in dame:
    print("NO")
else:
    dp = [-1]*(n-3) + [1,1,1,0]

    for i in range(n-4, -1, -1):
        if i not in dame:
            tmp = 100+1
            for j in range(3):
                if i+j+1 not in dame:
                    tmp = min(tmp, dp[i+j+1])
            dp[i] = tmp + 1
    if dp[0] <= 100:
        print("YES")
    else:
        print("NO")