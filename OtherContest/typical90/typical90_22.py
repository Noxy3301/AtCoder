import math

a,b,c = map(int, input().split())
gcd = math.gcd(a,math.gcd(b,c))
if gcd == 1:
    print(a+b+c-3)
else:
    print(a//gcd + b//gcd + c//gcd - 3)