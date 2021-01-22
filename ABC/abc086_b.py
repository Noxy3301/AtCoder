a,b = map(int, input().split())
x = int(str(a) + str(b))
hoge = 1
while hoge**2 < x:
    hoge += 1

if x == hoge**2:
    print("Yes")
else:
    print("No")