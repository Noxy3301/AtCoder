n = int(input())
d = tuple(map(int, input().split()))

ans = 2**50

for i in range(2**(n-1)):
    data = []
    tmp_index = 0
    i_zero = bin(i)[2:].zfill(n-1)
    for j in range(n-1):
        if i_zero[j] == "1":
            data.append(d[tmp_index:j+1])
            tmp_index = j+1
    data.append(d[tmp_index:j+2])

    or_list = []
    for j in range(len(data)):
        tmp_or = list(data[j])
        while len(tmp_or) > 1:
            tmp_or.append(tmp_or[0] | tmp_or[1])
            #tmp_or = 



    print(data)