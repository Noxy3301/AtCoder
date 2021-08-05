n,k = map(int, input().split())
c = tuple(map(int, input().split()))

dict = {}

for i in range(k):
    if c[i] in dict:
        dict[c[i]] += 1
    else:
        dict[c[i]] = 1

ans = len(dict)

for i in range(k, n):
    if c[i] in dict:
        dict[c[i]] += 1
    else:
        dict[c[i]] = 1
    dict[c[i-k]] -= 1
    if dict[c[i-k]] == 0:
        dict.pop(c[i-k])
    ans = max(ans, len(dict))


print(ans)