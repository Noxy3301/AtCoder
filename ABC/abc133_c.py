l, r = map(int, input().split())

if r-l+1 >= 673: #rとlの距離が673以上離れていると3の倍数と673の倍数の数が存在するから0になる
    print(0)
else: #高々672C2だからいけるはず
    d = list(range(l,r+1))
    ans = 10**10
    for i in range(len(d)-1):
        for j in range(i+1, len(d)):
            ans = min(ans, d[i]*d[j]%2019)
    print(ans)