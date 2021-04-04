import sys
n = int(input())
ans = 0
for i in range(1,10**7):
    if int(str(i)*2) <= n:
        ans += 1
    else:
        print(ans)
        sys.exit()