n = int(input())
k = int(input())
x = int(input())
y = int(input())
if n <= k:
    print(n*x)
else:
    print(x*k+(n-k)*y)