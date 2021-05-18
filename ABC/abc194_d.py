#確率1/pが出る期待値は逆数のp

n = int(input())

ans = 0

for i in range(1,n):
    ans += n/i

print(ans)