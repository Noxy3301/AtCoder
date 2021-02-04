n,m = map(int, input().split())
condition = [tuple(map(int, input().split())) for i in range(m)]
k = int(input())
put = [tuple(map(int, input().split())) for i in range(k)]
ans = 0

for i in range(2**k):
    tmp_ans = 0
    sara = [0]*n
    tmp = bin(i)[2:].zfill(k)
    for j in range(k):
        if tmp[j] == "0":
            sara[put[j][0]-1] += 1
        else:
            sara[put[j][1]-1] += 1
    for x in range(m):
        if sara[condition[x][0]-1] != 0 and sara[condition[x][1]-1] != 0:
            tmp_ans += 1
    ans = max(ans, tmp_ans)
print(ans)