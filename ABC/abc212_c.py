n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

data = []

for i in a:
    data.append([i,0])
for i in b:
    data.append([i,1])

data.sort()

ans = 10**10

for i in range(n+m-1):
    if data[i][1] != data[i+1][1]:
        ans = min(ans, abs(data[i][0]-data[i+1][0]))

print(ans)