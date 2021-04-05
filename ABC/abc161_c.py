n,k = map(int, input().split())
tmp = n - k*(n//k)
if tmp >= abs(tmp-k):
    print(abs(tmp-k))
else:
    print(tmp)