n = int(input())
ans = 0
x_y_list = [tuple(map(int, input().split())) for _ in range(n)]
d = set(x_y_list)

for i in range(n-1):
    sx, sy = x_y_list[i]
    for j in range(i+1, n):
        gx, gy = x_y_list[j]
        xd = sx - gx
        yd = sy - gy
        #if (gx-sy+gy,sx+gy-gx) in d and (sx+gy-sy,sy-gx+sx) in d:  ←これいちいち計算しているからMLEになる
        if (gx-yd,gy+xd) in d and (sx-yd,sy+xd) in d:
            ans = max(ans, (sx-gx)**2 + (sy-gy)**2)

print(ans)