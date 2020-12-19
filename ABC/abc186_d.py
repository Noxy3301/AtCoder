n = int(input())
d = tuple(map(int, input().split()))
sort_d = sorted(d)
diff = tuple([sort_d[i+1]-sort_d[i] for i in range(n-1)])
ans = 0

for i in range(1,n):
    ans += diff[i-1]*(n-i)*(i)

print(ans)