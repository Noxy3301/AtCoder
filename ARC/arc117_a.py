a,b = map(int, input().split())
tmpA = [i+1 for i in range(a)]
tmpB = [-(i+1) for i in range(b)]

if sum(tmpA) - abs(sum(tmpB)) > 0:
    tmpB[-1] -= (sum(tmpA) - abs(sum(tmpB)))
else:
    tmpA[-1] += abs(sum(tmpB)) - sum(tmpA)

hoge = " ".join([str(tmpA[i]) for i in range(a)]) + " " + " ".join([str(tmpB[i]) for i in range(b)])

print(hoge)