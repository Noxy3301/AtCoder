n, m = map(int, input().split())
d = [tuple(map(int, input().split())) for _ in range(m+1)]
ans = 0

for i in range(2**n):
    tmp_ans = 0
    tmp = bin(i)[2:].zfill(n)
    check = [0]*m
    switch = []
    for j in range(n):
        if tmp[j] == "1":
            switch.append(j+1)
    st = tuple(switch)

    for k in range(m):
        for x in range(d[k][0]):
            print("{} / {}".format(d[k][x], st))
            if d[k][x+1] in st:
                check[k] += 1
    for j in range(m):
        if check[j] % 2 == d[m][j]:
            tmp_ans += 1
    if tmp_ans == m:
        ans += 1

print(ans)