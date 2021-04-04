import math

under_fifty = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

n = int(input())
x = tuple(map(int, input().split()))

ans = 10**50

for i in range(1,2**len(under_fifty)):
    zero = bin(i)[2:].zfill(15)
    tmp = 1
    isCoprime = True
    for j in range(15):
        if zero[j] == "1":
            tmp = tmp * under_fifty[j]
    for j in x:
        if math.gcd(tmp, j) == 1: #互いに素なら
            isCoprime = False

    if isCoprime == True:
        ans = min(ans, tmp)

print(ans)