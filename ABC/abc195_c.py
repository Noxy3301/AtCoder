import math
n = input()
ans = 0
zero = n.zfill(len(n)+(3-(len(n)%3)))
san = [zero[i:i+3] for i in range(0,math.ceil(len(n)/3)*3,3)]

ans += ((int(n) - 10**(3*(len(san)-1)))+1)*(len(san)-1)

for i in range((len(san)-2),0,-1):
    ans += 999*10**(3*i)*i

print(ans)