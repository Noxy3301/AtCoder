a,b = map(int, input().split())
c,d = map(int, input().split())
x = max(a,b)
print(max(x-c, x-d))