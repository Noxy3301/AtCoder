def keisan(mozi,num):
    mozi = mozi[:4] + str(num)
    point = 0
    for i in range(1,9+1):
        point += i*10**mozi.count(str(i))
    return point

k = int(input())
s = input()
t = input()
card = [k]*9
for i in range(4):
    card[int(s[i])-1] -= 1
    card[int(t[i])-1] -= 1
tmp = 0

for i in range(1,9+1):
    for j in range(1,9+1):
        if i == j:
            if card[i-1] <= 1:
                continue
        else:
            if card[i-1] == 0 or card[j-1] == 0:
                continue
        if keisan(s,i) > keisan(t,j):
            if i == j: #同じ数字だった時
                tmp += card[i-1]*(card[j-1]-1)
            else:
                tmp += card[i-1]*card[j-1]
print(min(1,tmp/((9*k-8)*(9*k-9))))