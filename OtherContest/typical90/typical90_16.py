n = int(input())
a,b,c = map(int, input().split())
ans = 10**4

for i in range(10**4):
    for j in range(10**4 - i):
        if n - (a*i + b*j) >= 0:
            if (n - (a*i + b*j)) % c == 0:
                ans = min(ans, i + j + (n - (a*i + b*j))//c)
print(ans)