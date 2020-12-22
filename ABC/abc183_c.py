import itertools
n, k = map(int, input().split())
d = [tuple(map(int, input().split())) for _ in range(n)]
t_list = list(itertools.permutations(range(2,n+1)))
ans = 0

for i in range(len(t_list)):
    tmp = (1,) + t_list[i] + (1,)
    time = 0
    for j in range(len(tmp)-1):
        time += d[tmp[j]-1][tmp[j+1]-1]
    if time == k:
        ans += 1
print(ans)