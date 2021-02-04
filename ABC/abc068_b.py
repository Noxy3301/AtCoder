def div_two(x):
    hoge = 0
    while True:
        if x % 2 != 0:
            return hoge
        else:
            hoge += 1
            x = x//2

ans = 1
count = 0
n = int(input())
for i in range(1, n+1):
    if count < div_two(i):
        count = div_two(i)
        ans = i
print(ans)