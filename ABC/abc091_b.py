n = int(input())
s = tuple(input() for i in range(n))
m = int(input())
t = tuple(input() for i in range(m))

st = set(s+t)
ans = 0

for i in st:
    ans = max(ans, s.count(i)-t.count(i))
print(ans)