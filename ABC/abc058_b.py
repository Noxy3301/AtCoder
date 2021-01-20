o = input()
e = input()
ans = ""
for i in range(len(o) + len(e)):
    if i % 2 == 0:
        ans = ans + o[0]
        o = o[1:]
    else:
        ans = ans + e[0]
        e = e[1:]
print(ans)