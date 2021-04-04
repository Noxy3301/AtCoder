import math

n = int(input())
x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
sins = math.sin(math.radians((-(360/n) * (n/2 - 1))))
coss = math.cos(math.radians((-(360/n) * (n/2 - 1))))

xd = ((x2+x1) + (x2-x1)*coss - (y2-y1)*sins)/2
yd = ((y2+y1) + (y2-y1)*coss + (x2-x1)*sins)/2

print(xd,yd)