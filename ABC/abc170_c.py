x, n = map(int, input().split())
p = tuple(map(int, input().split()))

d = [i for i in range(-1, 102) if i not in p]

dekai = 1000

for i in d:
  if dekai > abs(int(i)-x):
    ans = i
    dekai = abs(int(i)-x)

print(ans)