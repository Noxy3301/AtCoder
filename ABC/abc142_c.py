n = int(input())
d = tuple(map(int, input().split()))

idx = [(d[i], i+1) for i in range(n)]
idx.sort()

ans = ""

for i in range(n):
    ans += str(idx[i][1]) + " "

print(ans)