import math

t = int(input())
l,x,y = map(int, input().split())
q = int(input())
e = []

for i in range(q):
    e.append(int(input()))

for i in e:
    deg = -360*i/t
    rad = deg*math.pi/180
    current_y = l*math.sin(rad)/2
    current_z = l*(1-math.cos(rad))/2
    san = math.sqrt(x**2 + (y - current_y)**2)
    print(math.degrees(math.atan(current_z/san)))