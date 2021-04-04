n,m,q = map(int, input().split())
nimotu = [tuple(map(int, input().split())) for i in range(n)]
hako = tuple(map(int, input().split()))

for i in range(q):
    l,r = map(int, input().split())
    l -= 1
    r -= 1
    box = []
    for j in range(m):
        if j < l or r < j:
            box.append(hako[j])
    print(box)
    box.sort()

    ans = 0
    s_nimotu = sorted(nimotu)
    
    print(s_nimotu)
    print(box)
    

print(nimotu)