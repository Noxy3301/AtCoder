n = int(input())
num = [0]*501
a = tuple(map(int, input().split()))
for i in a:
    num[i+200] += 1

ans = 0

for i in range(len(num)-1):
     for j in range(i+1, len(num)):
         ans += num[i]*num[j]*((i-200)-(j-200))**2

print(ans)