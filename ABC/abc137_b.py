k, x = map(int, input().split())
d = list(range(x-k+1,x+k))
print(*d)

#*でListをアンパックできる