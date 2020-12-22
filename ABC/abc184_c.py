import sys

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

#0手で行ける
if r1 == r2 and c1 == c2:
    print(0)
    sys.exit()

#1手で行ける
if r1+c1 == r2+c2 or r1-c1 == r2-c2 or abs(r1-r2)+abs(c1-c2) <= 3:
    print(1)
    sys.exit()

#2手で行ける
if (r1+c1+r2+c2)%2 == 0 or abs(r1-r2)+abs(c1-c2) <= 6 or abs((r1+c1)-(r2+c2)) <= 3 or abs((r1-c1)-(r2-c2)) <= 3:
    print(2)
    sys.exit()

print(3)