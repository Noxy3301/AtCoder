import sys
n,m = map(int, input().split())
d = [tuple(map(int, input().split())) for i in range(m)]

for i in range(10**n):
    string = str(i).ljust(n, "0")
    flag = True
    for j in d:
        if string[j[0]-1] != str(j[1]):
            flag = False
    if flag == True:
        if string == str(int(string)):
            print(string)
            sys.exit()

print(-1)