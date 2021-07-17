n = int(input())
a = tuple(map(int, input().split()))

mae = a[:len(a)//2]
usiro = a[(len(a)+1)//2:]
usiro = usiro[::-1]

ans = 0
for i in range(len(mae)):
    if mae[i] != usiro[i]:
        ans += 1
        if mae[i] not in usiro:
            ans += 1

print(max(0,ans-1))