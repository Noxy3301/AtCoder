#wa wakewakaran
n = int(input())
ans = 1

for i in range(1,n):
    ans *= (n*(i-n)+n**2)/(i-n)**2

print(ans)