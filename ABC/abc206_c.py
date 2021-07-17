def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1

n = int(input())
a = tuple(map(int, input().split()))

num = list(set(a))
num.sort()
kazu = [0]*len(num)

for i in a:
    kazu[binary_search(num,i)] += 1

ans = ((1+(n-1))*(n-1))//2

for i in kazu:
    ans -= ((1+(i-1))*(i-1))//2

print(ans)