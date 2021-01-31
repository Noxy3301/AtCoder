n = int(input())
s = [input() for i in range(n)]
ans = 0

while len(s) > 1:
    if s[-1] == "OR":
        ans += 2**len(s)
    s.pop(-1)

if s[0] == "AND":
    ans += 1
else:
    ans += 3

print(ans)