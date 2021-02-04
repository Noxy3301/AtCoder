a,b,c = map(int, input().split())
c_kouho = []
a_x = 1
while True:
    if a*a_x%b in c_kouho:
        break
    else:
        c_kouho.append(a*a_x%b)
        a_x += 1
if c in c_kouho:
    print("YES")
else:
    print("NO")