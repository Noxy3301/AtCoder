import math
 
l = int(input())
 
def fact_11(x):
    ans = 1
    for i in range(x-11,x):
        ans *= i
    return ans
 
print(fact_11(l)//math.factorial(11))