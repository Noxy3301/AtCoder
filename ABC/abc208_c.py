n,k = map(int, input().split())
a = list(map(int, input().split()))


zenbu = k//n
k = k%n
l = sorted(a)
zannen = l[k]

for i in range(n):
    if a[i] < zannen:
        print(zenbu + 1)
    else:
        print(zenbu)
