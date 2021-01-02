import numpy as np

n = int(input())
d = [tuple(map(int, input().split())) for _ in range(n)]
vote = [d[i][0] + d[i][1] for i in range(n)]
vote_impact = [d[i][0]*2 + d[i][1] for i in range(n)]
aoki = sum([d[i][0] for i in range(n)])
takahasi = 0
ans = 0
pin = 0

for i in np.argsort(vote_impact)[::-1]:
    ans += 1
    takahasi += vote[i]
    aoki -= d[i][0]
    if takahasi > aoki:
        print(ans)
        break