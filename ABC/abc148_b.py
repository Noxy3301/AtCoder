n = int(input())
s, t = map(str, input().split())
ans = ""
for i in range(n*2):
    if i % 2 == 0:
        ans += s[0]
        s = s[1:]
    else:
        ans += t[0]
        t = t[1:]
print(ans)