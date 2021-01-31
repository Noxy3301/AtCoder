n = int(input())
d = [2,1]
if n < 2:
    print(d[n])
else:
    for i in range(n-1):
        d.append(sum(d))
        d.pop(0)
    print(d[-1])