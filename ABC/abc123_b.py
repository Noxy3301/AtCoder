d = [int(input()) for i in range(5)]
ans = 0
while len(d) != 0:
    lastDigit = -1
    menu = -1
    for i in range(len(d)):
        if d[i]%10 == 0:
            menu = i
            break
        elif lastDigit < d[i]%10:
            lastDigit = d[i]%10
            menu = i
    ans += d[menu]
    if d[menu]%10 != 0 and len(d) != 1:
        ans += 10-d[menu]%10
    d.remove(d[menu])
print(ans)