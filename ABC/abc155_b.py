import sys
n = int(input())
d = tuple(map(int, input().split()))

for i in d:
    if i % 2 == 0:
        if not(i % 3 == 0 or i % 5 == 0):
            print("DENIED")
            sys.exit()
print("APPROVED")