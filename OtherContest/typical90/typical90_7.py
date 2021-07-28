def binary_search(arr, data):
    left = 0
    right = len(arr)-1
    while right-left > 1:
        if arr[(left+right)//2] < data:
            left = (left+right)//2
        elif arr[(left+right)//2] > data:
            right = (left+right)//2
        else:
            return 0
    return min(abs(arr[left]-data), abs(arr[right]-data))




n = int(input())
a = list(map(int, input().split()))
a.sort()
q = int(input())
ans = []

if n == 1:
    for i in range(q):
        ans.append(abs(int(input()) - a[0]))
else:
    for i in range(q):
        ans.append(binary_search(a, int(input())))

for i in ans:
    print(i)