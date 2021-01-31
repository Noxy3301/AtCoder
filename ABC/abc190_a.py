a,b,c = map(int, input().split())
while True:
    if a-1 < 0 or b-1 < 0:
        break
    if c == 1:
        b -= 1
        c = 0
    else:
        a -= 1
        c = 1
if a == 0 and b == 0:
    if c == 1:
        print("Takahashi")
    else:
        print("Aoki")
elif a == 0:
    print("Aoki")
else:
    print("Takahashi")