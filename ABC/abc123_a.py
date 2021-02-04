d = [int(input()) for i in range(5)]
k = int(input())
ans = "Yay!"
for i in range(4):
    for j in range(i+1, 5):
        if d[j] - d[i] > k:
            ans = ":("
print(ans)