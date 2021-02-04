n = int(input())
a = tuple(map(int, input().split()))
copy_a = a
while len(a) > 2:
    a = [max(a[i],a[i+1]) for i in range(0,len(a)-1,2)]
print(copy_a.index(min(a))+1)