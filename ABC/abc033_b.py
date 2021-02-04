n = int(input())
s_list = []
p_list = []
for i in range(n):
    s, p = input().split()
    s_list.append(s)
    p_list.append(int(p))

if sum(p_list)//2 < max(p_list):
    print(s_list[p_list.index(max(p_list))])
else:
    print("atcoder")
