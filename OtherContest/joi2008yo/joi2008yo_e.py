import copy

r,c = map(int, input().split())
d = [tuple(map(int, input().split())) for _ in range(r)]
ans = 0

for i in range(2**r):
    candicate = 0
    binary = bin(i)[2:].zfill(r)
    for j in range(c):
        count_one = 0
        count_zero = 0
        for k in range(r):
            if (d[k][j] == 1 and binary[k] == "0") or (d[k][j] == 0 and binary[k] == "1"):
                count_one += 1
            else:
                count_zero += 1
        candicate += max(count_one,count_zero)
    ans = max(ans, candicate)

print(ans)