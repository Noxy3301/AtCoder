n = int(input())
d = tuple(map(int, input().split()))
ans = 0
for i in d:
    ans += 1/i
print(1/ans)