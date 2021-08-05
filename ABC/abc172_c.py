def binary_search(arr, data):
    left = 0
    right = len(arr)-1
    while right-left > 1:
        if arr[(left+right)//2] < data:
            left = (left+right)//2
        elif arr[(left+right)//2] > data:
            right = (left+right)//2
    if arr[right] <= data:
        return right
    else:
        return left

n,m,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ruiseki_a, ruiseki_b = [0], [0]

for i in range(n):
    ruiseki_a.append(ruiseki_a[-1] + a[i])
for i in range(m):
    ruiseki_b.append(ruiseki_b[-1] + b[i])

ans = -1

for i in range(len(ruiseki_a)):
    if ruiseki_a[i] <= k:
        t = k - ruiseki_a[i]
        ans = max(ans, i + binary_search(ruiseki_b, t))
print(ans)