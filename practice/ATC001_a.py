h,w = map(int, input().split())
meiro = []
flag = []

def tansaku(x,y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return
    if flag[x][y] == True:
        return
    flag[x][y] = True

    tansaku(x+1,y) #migi
    tansaku(x-1,y) #hidari
    tansaku(x,y+1) #sita
    tansaku(x,y-1) #ue