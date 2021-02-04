n,s,d = map(int, input().split())
isDamage = False
for i in range(n):
    x,y = map(int, input().split())
    if x < s and y > d:
        isDamage = True
if isDamage:
    print("Yes")
else:
    print("No")