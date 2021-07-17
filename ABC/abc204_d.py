n = int(input())
d = tuple(map(int, input().split()))
s = sorted(d, reverse=True)
a = []
b = []

for i in s:
    if sum(a) == sum(b):
        a.append(i)
    elif sum(a) > sum(b):
        b.append(i)
    else:
        a.append(i)
    
print(a,b)