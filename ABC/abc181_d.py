import itertools

s = input()
isDiv = False
d = [0]*10
for i in s:
    if d[int(i)] < 3:
        d[int(i)] += 1
mozi = ""
for i in range(1,10):
    mozi += str(i)*min(3,d[i])

if len(s) == 1:
    if int(s)%8 == 0:
        isDiv = True
elif len(s) == 2:
    if int(s)%8 == 0 or int(s[::-1])%8 == 0:
        isDiv = True
else:
    for i in list(itertools.combinations(mozi,3)):
        for j in list(itertools.permutations(i)):
            tmp = "".join(j)
            if int(tmp)%8 == 0:
                isDiv = True
if isDiv:
    print("Yes")
else:
    print("No")