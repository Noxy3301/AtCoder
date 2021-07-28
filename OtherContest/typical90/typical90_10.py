n = int(input())
class_a = []
class_b = []

for i in range(n):
    c,p = map(int, input().split())
    if c == 1:
        class_a.append(p)
        class_b.append(0)
    else:
        class_a.append(0)
        class_b.append(p)

ruiseki_a = [0]
ruiseki_b = [0]
tmp_a, tmp_b = 0, 0

for i in range(n):
    tmp_a += class_a[i]
    tmp_b += class_b[i]
    ruiseki_a.append(tmp_a)
    ruiseki_b.append(tmp_b)

q = int(input())
for i in range(q):
    l,r = map(int, input().split())
    print("{} {}".format(ruiseki_a[r]-ruiseki_a[l-1],ruiseki_b[r]-ruiseki_b[l-1]))