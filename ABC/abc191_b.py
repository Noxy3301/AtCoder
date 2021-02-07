n,x = map(int, input().split())
d = tuple(map(int, input().split()))
d_a = ""
for i in d:
    if i != x:
        d_a += str(i) + " "
print(d_a)