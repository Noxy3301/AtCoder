sx, sy, gx, gy = map(int, input().split())
x = gx-sx
y_time = sy/(sy+gy)
print(x*y_time+sx)