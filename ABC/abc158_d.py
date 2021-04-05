s = input()
q = int(input())

reverse = False

mae = ""
usiro = ""

for i in range(q):
    query = input()
    if len(query) == 1:
        if reverse == False:
            reverse = True
        else:
            reverse = False
    else:
        if query[2] == "1":
            if reverse == False:
                mae = query[4] + mae
            else:
                usiro = usiro + query[4]
        else:
            if reverse == False:
                usiro = usiro + query[4]
            else:
                mae = query[4] + mae

s = mae + s + usiro
if reverse == True:
    print(s[::-1])
else:
    print(s)