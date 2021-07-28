h,w = map(int, input().split())
a = []
for i in range(h):
    a.append(list(map(int, input().split())))

sum_col = []
sum_row = []

for i in range(h):
    sum_row.append(sum(a[i]))

for i in range(w):
    tmp = 0
    for j in range(h):
        tmp += a[j][i]
    sum_col.append(tmp)

for i in range(h):
    ans = []
    for j in range(w):
        ans.append(str(sum_col[j] + sum_row[i] - a[i][j]))
    ex = " ".join(ans)
    print(ex)