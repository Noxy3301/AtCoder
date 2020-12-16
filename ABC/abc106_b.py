def count_divisors(n):
    divisors = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:  #昇順から数えて約数かどうか
            divisors += 1
            if i != n // i: #上記の対になる約数、約数が奇数個の時重複してカウントしないようにしている
                divisors += 1
    return divisors


n = int(input())
ans = 0

for i in range(1,n+1):
    if i % 2 == 1:
        if count_divisors(i) == 8:
            ans += 1

print(ans)