s = input()

ans = ""
reverse = False

for i in s:
    if i != "R":
        if reverse == False:
            ans = ans + i
            if len(ans) >= 2:
                if ans[-1] == ans[-2]:
                    ans = ans[:-2]
        else:
            ans = i + ans
            if len(ans) >= 2:
                if ans[0] == ans[1]:
                    ans = ans[2:]
    else:
        if reverse == False:
            reverse = True
        else:
            reverse = False

if reverse == True:
    ans = ans[::-1]

print(ans)