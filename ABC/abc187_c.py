import sys

n = int(input())

nor = []
exp = []

for i in range(n):
    x = input()
    if x[0] == "!":
        exp.append(x[1:])
    else:
        nor.append(x)

st_nor = set(nor)
st_exp = set(exp)

for i in st_nor:
    if i in st_exp:
        print(i)
        sys.exit()
print("satisfiable")