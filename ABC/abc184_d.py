a,b,c = map(int, input().split())
dp = [[[0]*101 for i in range(101)] for j in range(101)]
dp[99][99][99] = 1

# for i in range(99,0,-1):
#     for j in range(99,0,-1):
#         for k in range(99,0,-1):
#             dp[][][]