n,D,H = map(int, input().split())
obs = [map(int, input().split()) for i in range(n)]

ans = 0

for i in range(n):
    d,h = obs[i]
    tmp = (h-H)/(d-D) * -D + H
    ans = max(ans, tmp)

print(ans)