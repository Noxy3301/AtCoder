h,w = map(int, input().split())
meiro = []
flag = []
sx, sy = 0, 0
gx, gy = 0, 0

def tansaku(y,x):
    if y < 0 or y > w-1 or x < 0 or x > h-1:
        return
    if meiro[y][x] == "#":
        return
    if flag[y][x] == True:
        return
    flag[y][x] = True

    tansaku(y,x+1) #ue
    tansaku(y,x-1) #sita
    tansaku(y+1,x) #migi
    tansaku(y-1,x) #hidari

for i in range(h):
    hoge = input()
    meiro.append(hoge)
    flag.append([False]*w)
    if "s" in hoge:
        sy = hoge.index("s")
        sx = i
    if "g" in hoge:
        gy = hoge.index("g")
        gx = i

tansaku(sx,sy)

if flag[gx][gy] == True:
    print("Yes")
else:
    print("No")