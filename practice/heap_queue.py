#abc212_d
import heapq
#heapqを使うことで最小値とか最大値をO(1)でとることができる

q = int(input())
d = []
add = 0
ans = []

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(d, query[1] - add)
    elif query[0] == 2:
        add += query[1]
    else:
        ans.append(heapq.heappop(d) + add)

for i in ans:
    print(i)