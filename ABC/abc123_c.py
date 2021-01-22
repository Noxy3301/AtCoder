import math
n = int(input())
d = [int(input()) for i in range(5)]
print(math.ceil(n/min(d)) + 4)