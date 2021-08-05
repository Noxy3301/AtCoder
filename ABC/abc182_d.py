n = int(input())
a = list(map(int, input().split()))
cum, cum_cum = [0], [0]
for i in range(n):
    cum.append(cum[-1] + a[i])
for i in range(1, n+1):
    cum_cum.append(cum_cum[-1] + cum[i])

print(max(cum_cum) + max(cum))