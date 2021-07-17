x,y = map(int, input().split())
hoge = [0]*3

hoge[x] += 1
hoge[y] += 1

if x == y:
    print(x)
else:
    for i in range(len(hoge)):
        if hoge[i] == 0:
            print(i)