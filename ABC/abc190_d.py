def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
div = make_divisors(2*n)
ans = 0

for i in range(len(div)//2):
    if (div[i]-div[-i-1])%2 == 1:
        ans += 2
print(ans)