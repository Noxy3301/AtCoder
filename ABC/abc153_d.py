h = int(input())
tmp = h
ans = 0
hoge = []

while h > 1:
    hoge.append(h//2)
    h = h//2

for i in range(len(hoge)):
    ans += 2**i

if tmp == 1:
    ans += 1
else:
    ans += 2**(i+1)

print(ans)