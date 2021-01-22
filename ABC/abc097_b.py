x = int(input())
ans = 1
for i in range(x//2):
    for j in range(x//2):
        if x >= i**j:
            ans = max(ans, i**j)
print(ans)