x,y,a,b = map(int, input().split())
exp = 0

while x*a <= x+b and x*a < y:
    exp += 1
    x = x*a

exp += (y-1-x)//b
print(exp)