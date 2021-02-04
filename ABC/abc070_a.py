x = int(input())
d = str(x)[::-1]
d_2 = str(x)
isTrue = True

for i in range(len(d)):
    if d[i] != d_2[i]:
        isTrue = False
        break
if isTrue:
    print("Yes")
else:
    print("No")