x = int(input())
ans = 0

if x >= 500:
    ans += 1000*(x//500)
    x -= 500 * (x//500)

print(ans + 5*(x//5))