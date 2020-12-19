h,w = map(int, input().split())
d = [tuple(map(int, input().split())) for _ in range(h)]
min_d = 101
ans = 0
for i in d:
    min_d = min(min_d, min(i))

for i in d:
    for j in range(w):
        ans += i[j] - min_d
print(ans)