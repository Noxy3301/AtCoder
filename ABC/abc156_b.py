def base10_to_n(x,n):
    tmp = x
    ans = ""
    while tmp > 0:
        ans = str(tmp%n) + ans
        tmp = tmp//n
    return ans


n,k = map(int, input().split())
print(len(base10_to_n(n,k)))