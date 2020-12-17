n = input()
d = []
ans = 19
for i in n:
    d.append(int(i))
 
for i in range(2**len(d)):
    temp = int(n)
    hoge = 0
    for j in range(len(d)):
        if ((int(bin(i)[2:]) >> j) & 1):
            temp -= int(d[j])
            hoge += 1
    if temp % 3 == 0 and hoge < ans and hoge != len(d):
        ans = hoge
 
if ans == 19:
    print(-1)
else:
    print(ans)