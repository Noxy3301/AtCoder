bingo = []

for i in range(3):
    a,b,c = map(int, input().split())
    bingo.append(a)
    bingo.append(b)
    bingo.append(c)

card = [0]*9

n = int(input())
for i in range(n):
    hoge = int(input())
    if hoge in bingo:
        card[bingo.index(hoge)] += 1

yoko_1 = card[0] & card[1] & card[2]
yoko_2 = card[3] & card[4] & card[5]
yoko_3 = card[6] & card[7] & card[8]

tate_1 = card[0] & card[3] & card[6]
tate_2 = card[1] & card[4] & card[7]
tate_3 = card[2] & card[5] & card[8]

naname_1 = card[0] & card[4] & card[8]
naname_2 = card[2] & card[4] & card[6]

if tate_1 or tate_2 or tate_3 or yoko_1 or yoko_2 or yoko_3 or naname_1 or naname_2:
    print("Yes")
else:
    print("No")