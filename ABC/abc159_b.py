import sys

s = input()

def isKaibun(txt):
    if txt == txt[::-1]:
        return True
    else:
        return False

if isKaibun(s):
    mae = s[:(len(s)-1)//2]
    usiro = s[(len(s)+3-1)//2:]
    if isKaibun(mae) and isKaibun(usiro):
        print("Yes")
        sys.exit()
print("No")