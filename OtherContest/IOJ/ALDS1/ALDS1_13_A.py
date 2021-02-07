import itertools

n = int(input())
exist_queen = [tuple(map(int, input().split())) for _ in range(n)]

for i in list(itertools.permutations(range(8))):
    isEightQueen = True
    for j in range(7):
        for k in range(j+1,8):
            if abs(i[j]-i[k]) == abs(j-k):
                isEightQueen = False
    if isEightQueen:
        isComplete = True
        cordinate = [(v,i[v]) for v in range(8)]
        for each in exist_queen:
            if each not in cordinate:
                isComplete = False
        if isComplete:
            for x in range(8):
                ans = ""
                for y in range(8):
                    if (x,y) in cordinate:
                        ans += "Q"
                    else:
                        ans += "."
                print(ans)