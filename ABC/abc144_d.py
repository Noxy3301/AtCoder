import math

a,b,x = map(int, input().split())
if a*a*b/2 <= x: #半分以下
    tmpA = (2*x)/(a*b)
    tmpB = b**2 + tmpA**2
    sinA = tmpA/tmpB
    print(tmpA,tmpB,sinA)
    print(math.degrees(math.asin(sinA)))
else:
    pass