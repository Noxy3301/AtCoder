import heapq
n,m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    a[i] *= -1  #heapqは最小値しか取れないから-1倍して最大値をとれるようにする

heapq.heapify(a)

for i in range(m):
    heapq.heappush(a, -(-heapq.heappop(a)//2))

print(-1*sum(a))