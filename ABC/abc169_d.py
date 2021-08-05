def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr

n_input = int(input())
if n_input == 1:
    print(0)
else:
    d = factorization(n_input)
    ans = 0

    for i in d:
        n = 1
        while (1+n)*n//2 <= i[1]:
            n += 1
        ans += n-1

    print(ans)