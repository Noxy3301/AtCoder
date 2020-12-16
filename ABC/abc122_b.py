s = input()
ans = 0
temp = 0
for i in s:
    if i == "A" or i == "C" or i == "G" or i == "T":
        temp += 1
        if ans < temp:
            ans = temp
    else:
        temp = 0
print(ans)