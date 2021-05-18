def isKaibun(txt):
    if txt == txt[::-1]:
        return True
    else:
        return False

n = input()

flag = False

if isKaibun(n):
    flag = True

for i in range(9):
    n = "0" + n
    if isKaibun(n):
        flag = True

if flag:
    print("Yes")
else:
    print("No")