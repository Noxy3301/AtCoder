import sys
x = input()
if len(set(x)) == 1:
    print("Weak")
    sys.exit()
else:
    flag = []
    for i in range(3):
        if (int(x[i])+1)%10 == (int(x[i+1]))%10:
            flag.append(0)
    if len(flag) == 3:
        print("Weak")
    else:
        print("Strong")