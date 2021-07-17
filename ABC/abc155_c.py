n = int(input())
d = {}

for i in range(n):
    tmp = input()
    if tmp not in d:
        d[tmp] = 1
    else:
        d[tmp] += 1

max_value = max(d.values())
ans = [i for i in d if d[i] == max_value]

ans.sort()

for i in ans:
    print(i)