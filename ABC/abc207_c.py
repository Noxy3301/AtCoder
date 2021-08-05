n = int(input())
l_list, r_list = [], []

for i in range(n):
    t,l,r = map(int, input().split())
    if t == 2:
        r -= 0.1
    elif t == 3:
        l += 0.1
    elif t == 4:
        l += 0.1
        r -= 0.1
    l_list.append(l)
    r_list.append(r)

ans = 0

for i in range(n-1):
    for j in range(i+1, n):
        if max(l_list[i],l_list[j]) <= min(r_list[i],r_list[j]):
            ans += 1
print(ans)