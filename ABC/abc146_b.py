n = int(input())
s = input()
ans = ""
for i in s:
    if ord(i)+n > 90:
        ans = ans + chr((ord(i)+n)%90 + 64)
    else:
        ans = ans + chr(ord(i)+n)
print(ans)