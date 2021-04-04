n = int(input())
a = tuple(map(int, input().split()))

data = [0]*(10**5+1)

ans = sum(a)

for i in range(n):
    data[a[i]] += 1

q = int(input())
queue = [tuple(map(int, input().split())) for i in range(q)]

for i in range(q):
    b,c = queue[i]
    ans += (c-b)*data[b]
    data[c] += data[b]
    data[b] = 0
    print(ans)