import math

n = int(input())
d = tuple(map(int, input().split()))
u_200 = [d[i]%200 for i in range(n)] #under_200
c_200 = [0]*200 #count_200

for i in range(n):
    c_200[u_200[i]] += 1

ans = 0

for i in c_200:
    if i > 1:
        ans += math.factorial(i) // (math.factorial(2) * math.factorial(i-2))

print(ans)