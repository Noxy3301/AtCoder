import math

n = int(input())
d = list(map(int, input().split()))
man, euk, che = 0, 0, 0
for i in d:
    man += abs(i)
    euk += abs(i)**2
    if che < abs(i):
        che = abs(i)

print(man)
print(math.sqrt(euk))
print(che)