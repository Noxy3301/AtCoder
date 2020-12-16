import math
 
a,b,h,m = map(int, input().split())
 
hAngle = 360*((h/12) + (1/12) * (m/60))
mAngle = 360*(m/60)
 
angle = abs(hAngle - mAngle)
 
c = a*a + b*b - 2*a*b*math.cos(math.radians(angle))
 
print(math.sqrt(c))