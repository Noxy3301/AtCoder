n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

b_c = [b[c[i]-1] for i in range(n)]

a_dic = {}
b_dic = {}
ans = 0

for i in range(n):
    if a[i] not in a_dic:
        a_dic[a[i]] = 1
    else:
        a_dic[a[i]] += 1
    if b_c[i] not in b_dic:
        b_dic[b_c[i]] = 1
    else:
        b_dic[b_c[i]] += 1

a_keys = a_dic.keys()
b_keys = b_dic.keys()
for i in a_keys:
    if i in b_keys:
        ans += a_dic[i] * b_dic[i]

print(ans)