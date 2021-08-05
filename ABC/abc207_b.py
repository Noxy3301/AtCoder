import sys
a,b,c,d = map(int, input().split())
mizuiro = a+b
akairo = c
ans = 1

for i in range(a):
    if mizuiro/akairo <= d:
        print(ans)
        sys.exit()
    else:
        mizuiro += b
        akairo += c
        ans += 1

print(-1)