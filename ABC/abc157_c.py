#wa
import sys
 
n,m = map(int, input().split())
 
num = ["0"]*n
flag = [0]*n
 
for i in range(m):
    s,c = map(int, input().split())
    if flag[s-1] != 0 and num[s-1] != str(c):
        print(-1)
        sys.exit()
    else:
        flag[s-1] = 1
        num[s-1] = str(c)
 
ans = "".join(num)
 
if ans != str(int(ans)):
    print(-1)
else:
    print(ans)