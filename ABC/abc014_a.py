a = int(input())
b = int(input())
ans = 0
while a%b != 0:
    a += 1
    ans += 1
print(ans)