#WA
n,m = map(int, input().split())
dict = {}

islands = 1
for i in range(m):
    a,b = map(int, input().split())
    isA_in_dict = a in dict
    isB_in_dict = b in dict
    if isA_in_dict == False and isB_in_dict == False:
        dict[a] = islands
        dict[b] = islands
        islands += 1
    elif isA_in_dict == True and isB_in_dict == False:
        dict[b] = dict[a]
    elif isA_in_dict == False and isB_in_dict == True:
        dict[a] = dict[b]

islands_count = [0]*islands
for i in dict.items():
    islands_count[i[1]-1] += 1

print(max(islands_count))