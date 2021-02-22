s = input()
flag = 1 #0が偶数、1が奇数
isComplete = True
for i in s:
    if flag == 1:
        if i.isupper():
            isComplete = False
            break
        flag = 0
    else:
        if i.islower():
            isComplete = False
            break
        flag = 1
if isComplete:
    print("Yes")
else:
    print("No")