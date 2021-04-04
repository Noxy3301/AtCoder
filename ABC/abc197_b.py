h,w,x,y = map(int, input().split())
s = ["b"*(w+2)]
for i in range(h):
    s.append("b" + input() + "b")
s.append("b"*(w+2))

ans = -3

for i in range(4):
    tmp_x = x
    tmp_y = y
    while s[tmp_x][tmp_y] == ".":
        ans += 1
        if i == 0:
            tmp_x -= 1
        elif i == 1:
            tmp_x += 1
        elif i == 2:
            tmp_y -= 1
        else:
            tmp_y += 1

print(ans)