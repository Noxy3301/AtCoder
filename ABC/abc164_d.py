s = input()
wa, ans = 0, 0
tmp_s = 0

for i in range(len(s)):
    wa += int(s[i])
    if wa % 3 == 0:
        print(int(s[tmp_s:i+1]))
        if int(s[tmp_s:i+1]) % 2019 == 0:
            ans += 1
            wa = 0
            tmp_s = i
print(ans)