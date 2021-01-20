n = int(input())
d = [int(input()) for i in range(n)]
d.sort(reverse=True)
print(d[0]//2 + sum(d[1:]))