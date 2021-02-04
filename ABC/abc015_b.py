import math
n = int(input())
a_original = list(map(int, input().split()))
a = [i for i in a_original if i != 0]
print(math.ceil(sum(a)/len(a)))