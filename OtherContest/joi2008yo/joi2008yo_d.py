m = int(input())
find_s = []
for i in range(m):
    find_s.append(list(map(int, input().split())))
n = int(input())
all_s = []
for i in range(n):
    all_s.append(list(map(int, input().split())))
rel_s = []
for i in range(len(find_s)):
    rel_s.append([find_s[i][0]-find_s[0][0],find_s[i][1]-find_s[0][1]])

for i in range(len(all_s)):
    count = 0
    for j in range(len(rel_s)):
        if [all_s[i][0]+rel_s[j][0],all_s[i][1]+rel_s[j][1]] in all_s:
            count += 1
            if count == len(find_s):
                print("{} {}".format(all_s[i][0]-find_s[0][0],all_s[i][1]-find_s[0][1]))
                break
    else:
        continue
    break