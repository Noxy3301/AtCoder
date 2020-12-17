import math
n, m = map(int, input().split())
d = tuple(map(int, input().split())) + (0,n+1)
s_tuple = tuple(sorted(d))
margin = tuple([s_tuple[i+1]-s_tuple[i]-1 for i in range(m+1) if s_tuple[i+1]-s_tuple[i]-1 != 0]) #隣接していない白マス
if len(margin) == 0: #ハンコ使わなくてOK
    print(0)
else:
    minimum = min(margin)
    if minimum == 1:
        hoge = sum(margin)
    else:
        hoge = sum(tuple(math.ceil(margin[i]/minimum) for i in range(len(margin))))
    if hoge == 0:
        print(1)
    else:
        print(hoge)