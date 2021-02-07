import math
x,y,r = map(float, input().split())
x = x*10**4
y = y*10**4
r = r*10**4

ans = 0
if r != 0:
    x_min = math.ceil(x-r)
    x_max = math.floor(x+r)
    for i in range(x_min, x_max+1,10**4):
        p = math.sqrt(r**2 - (x-i)**2)
        y_min = math.ceil(y-p)
        y_max = math.floor(y+p)
        ans += y_max-y_min+1
print(ans//10**4)