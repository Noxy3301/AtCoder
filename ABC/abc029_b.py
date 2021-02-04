s = [input() for i in range(12)]
ans = 0
for i in range(12):
    if "r" in s[i]:
        ans += 1
print(ans)