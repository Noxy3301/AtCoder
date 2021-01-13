import copy

#

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 10*10**10

for i in range(2**(n-1)):
    tmp = copy.deepcopy(a)
    binary_prev = bin(i)[2:].zfill(n-1)
    #binaryを反転させたいねえ
    binary = binary_prev[::-1]
    minimum = a[0]
    candicate = 0
    for j in range(n-1):
        minimum = max(minimum, tmp[j+1])
        if binary[j] == "1":
            candicate += minimum + 1 - tmp[j+1]
            tmp[j+1] = minimum + 1
            minimum = tmp[j+1]
    count = 1
    tiisai = tmp[0]
    for j in range(n-1):
        if tmp[j+1] > tiisai:
            count += 1
            tiisai = tmp[j+1]
    if count == k:
        ans = min(ans, candicate)
print(ans)