n,k = map(int, input().split())
for i in range(k):
    dekai = list(str(n))
    tiisai = list(str(n))
    dekai.sort(reverse=True)
    tiisai.sort()
    n = int("".join(dekai)) - int("".join(tiisai))
print(n)