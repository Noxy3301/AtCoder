#WA
n,k = map(int, input().split())
a = tuple(map(int, input().split()))

flag = [0]*n
flag[0] = 1
loop = [1]
index_bloop = -1

while True:
    if flag[a[loop[-1]-1]-1] != 0:
        index_bloop = loop.index(a[loop[-1]-1])
        break
    flag[loop[-1]-1] = 1
    loop.append(a[loop[-1]-1])

print(loop, index_bloop)

if k < index_bloop:
    print(loop[k-1])
else:
    print(loop[index_bloop + (k-index_bloop)%(len(loop)-index_bloop)])