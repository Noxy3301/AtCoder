import math
a,b,k = map(int, input().split())

ans = ""

while a > 0 and b > 0:
    if math.factorial(a+b-1)//(math.factorial(a-1)*math.factorial(b)) < k:
        ans += "b"
        k -= math.factorial(a+b-1)//(math.factorial(a-1)*math.factorial(b))
        b -= 1
    else:
        ans += "a"
        a -= 1

print(ans + "a"*a + "b"*b)