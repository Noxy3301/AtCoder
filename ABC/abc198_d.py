#TLE

import sys
import itertools

s1 = input()
s2 = input()
s3 = input()

char = list(set(list(s1+s2+s3)))

if len(char) > 10:
    print("UNSOLVABLE")
    sys.exit()

hoge = list(itertools.combinations(list(range(0,10)),len(char)))

for i in range(len(hoge)):
    huga = list(itertools.permutations(hoge[i]))
    for j in huga:
        siki = s1 + "+" + s2 + "=" + s3
        for k in range(len(j)):
            tmp = siki.replace(char[k],str(j[k]))
            siki = tmp
        str1 = siki[:siki.index("+")]
        str2 = siki[siki.index("+")+1:siki.index("=")]
        str3 = siki[siki.index("=")+1:]

        if str1[0] != "0" and str2[0] != "0" and str3[0] != "0":
            if int(str1) + int(str2) == int(str3):
                print(str1)
                print(str2)
                print(str3)
                sys.exit()

print("UNSOLVABLE")