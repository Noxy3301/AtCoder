import math
import itertools

n = int(input())
d = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0

for i in list(itertools.permutations(range(n))):
    tmp_ans = 0
    for j in range(n-1):
        tmp_ans += math.sqrt(((d[i[j]][0]-d[i[j+1]][0])**2 + (d[i[j]][1]-d[i[j+1]][1])**2))
    ans += tmp_ans/math.factorial(n)
print(ans)