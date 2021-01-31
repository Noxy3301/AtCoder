d = [0,0,1]
n = int(input())
if n <= 3:
    print(d[n-1])
else:
    for i in range(n-3):
        d.append(sum(d)%10007)
        d.pop(0)
    print(d[-1])