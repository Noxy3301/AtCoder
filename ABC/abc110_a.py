d = list(map(int, input().split()))
d.sort(reverse=True)
print(d[0]*10 + d[1] + d[2])