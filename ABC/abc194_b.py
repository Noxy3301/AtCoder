n = int(input())
task_a = []
task_b = []
for i in range(n):
    a,b = map(int, input().split())
    task_a.append(a)
    task_b.append(b)

list_a = list(enumerate(task_a))
sorted_a = sorted(list_a, key=lambda x:(x[1]))
list_b = list(enumerate(task_b))
sorted_b = sorted(list_b, key=lambda x:(x[1]))

if sorted_a[0][0] == sorted_b[0][0]:
    print(min(sorted_a[0][1]+sorted_b[0][1], max(sorted_a[0][1],sorted_b[1][1]),max(sorted_a[1][1],sorted_b[0][1])))
else:
    print(max(sorted_a[0][1],sorted_b[0][1]))