a,b,c = map(int, input().split())
dp = [[[0]*101 for i in range(101)] for j in range(101)]
dp[99][99][99] = 1

for i in range(99,a-1,-1):
    for j in range(99,b-1,-1):
        for k in range(99,c-1,-1):
            dp_i = (i/(i+j+k))*(dp[i+1][j][k]+1)
            dp_j = (j/(i+j+k))*(dp[i][j+1][k]+1)
            dp_k = (k/(i+j+k))*(dp[i][j][k+1]+1)
            dp[i][j][k] = dp_i + dp_j + dp_k
print(dp[a][b][c])