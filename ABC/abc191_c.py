h,w = map(int, input().split())
d = [input() for _ in range(h)]
ans = 0

for i in range(h-1):
    prev_hen = False
    for j in range(w):
        if d[i][j] != d[i+1][j]:
            if prev_hen == False:
                ans += 1
                prev_hen = True
        else:
            prev_hen = False

for i in range(w-1):
    prev_hen = False
    for j in range(h):
        if d[j][i] != d[j][i+1]:
            if prev_hen == False:
                ans += 1
                prev_hen = True
        else:
            prev_hen = False
print(ans)