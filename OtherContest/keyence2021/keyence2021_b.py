from collections import Counter
import sys

n, k = map(int, input().split())
a = tuple(map(int, input().split()))
st = set(a)

c = Counter(a)

dekai = max(st)
ans = 0

for i in range(dekai+1):
    hoge = c[i]
    if hoge == 0:
        ans += k*i
        print(ans)
        sys.exit()
    if hoge < k:
        ans += (k - hoge)*i
        k = c[i]

if k != 0:
    ans += k*(dekai+1)

print(ans)