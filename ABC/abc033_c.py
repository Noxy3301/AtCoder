s = input() + "+"
ans = 0
siki = ""
for i in range(len(s)):
    if s[i] != "+":
        siki += s[i]
    else:
        if "0" not in siki:
            ans += 1
        siki = ""
print(ans)