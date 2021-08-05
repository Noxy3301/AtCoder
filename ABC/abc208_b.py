import math
p = int(input())
ans = 0

i = 1
while math.factorial(i+1) < p:
    i += 1


while p != 0:
    ans += p//math.factorial(i)
    p = p%math.factorial(i)
    i -= 1

print(ans)