s = list(input())
maru, batu, hatena = s.count("o"), s.count("x"), s.count("?")

ans = 0

if maru <= 4:
    for i in range(0,10000):
        keta = str(i).zfill(4)
        flag = True
        for j in keta:
            if s[int(j)] == "x":
                flag = False
        for j in range(10):
            if s[j] == "o" and str(j) not in keta:
                flag = False
        if flag:
            ans += 1

print(ans)