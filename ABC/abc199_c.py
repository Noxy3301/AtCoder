n = int(input())
s = list(input())
q = int(input())

reverse = False

for i in range(q):
    t,a,b = map(int, input().split())
    if t == 1:
        if reverse == False:
            tmp = s[a-1]
            s[a-1] = s[b-1]
            s[b-1] = tmp
        else:
            if a < n:
                queueA = n+a-1
            else:
                queueA = a-n-1
            if b < n:
                queueB = n+b-1
            else:
                queueB = b-n-1
            tmp = s[queueA]
            s[queueA] = s[queueB]
            s[queueB] = tmp
    else:
        if reverse == False:
            reverse = True
        else:
            reverse = False

if reverse == True:
    hoge = s[n:] + s[:n]
    ans = "".join(hoge)
else:
    ans = "".join(s)
print(ans)