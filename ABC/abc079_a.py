x = input()

tmp = x[0]
count = 0
isTrue = False

for i in x:
    if i == tmp:
        count += 1
        if count >= 3:
            isTrue = True
    else:
        count = 1
        tmp = i

if isTrue:
    print("Yes")
else:
    print("No")