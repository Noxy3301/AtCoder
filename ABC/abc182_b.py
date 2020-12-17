n = int(input())
d = list(map(int, input().split()))
lim = max(d)
dekai, yabai = 0, 0
for i in range(2,lim+1):
    ans = 0
    for j in d:
        if j % i == 0:
            ans += 1
    if dekai < ans:
        dekai = ans
        yabai = i
print(yabai)