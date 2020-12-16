#O(1000*30000)だからMaxの時はTLEを起こす
#PyPyでAC

n = int(input())
s = input()
d = []
ans = 0
for i in range(1000):
    i_zero = str(i).zfill(3)
    flag = 0 #if flag == 3 then hit
    for j in range(n):
        if flag <= 2:
            if s[j] == i_zero[flag]:
                flag += 1
        if flag == 3:
            ans += 1
            break
print(ans)