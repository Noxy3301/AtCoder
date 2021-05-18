n = int(input())
data = []
a,b,c,d,e = [],[],[],[],[]
score = [0]*n

for i in range(n):
    A,B,C,D,E = map(int,input().split())
    data.append([A,B,C,D,E])
    a.append([A,i])
    b.append([B,i])
    c.append([C,i])
    d.append([D,i])
    e.append([E,i])

print(a,b,c,e,d)
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
d.sort(reverse=True)
e.sort(reverse=True)

for i in range(n):
    score[a[i][1]] += n-i+1
    score[b[i][1]] += n-i+1
    score[c[i][1]] += n-i+1
    score[d[i][1]] += n-i+1
    score[e[i][1]] += n-i+1

score_withIndex = [[score[i],i] for i in range(n)]

score_withIndex.sort(reverse=True)

print(score_withIndex)


# print(score)
    

# #最小値を引き上げる必要がある

# for i in range(n):
#     print(sum(d[i]))


# ans = 0

# for i in range(n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             minA = max(d[i][0],d[j][0],d[k][0])
#             minB = max(d[i][1],d[j][1],d[k][1])
#             minC = max(d[i][2],d[j][2],d[k][2])
#             minD = max(d[i][3],d[j][3],d[k][3])
#             minE = max(d[i][4],d[j][4],d[k][4])
#             tmp = ans

#             if ans < min(minA,minB,minC,minD,minE):
#                 print(i,j,k)
#                 ans = min(minA,minB,minC,minD,minE)

# print(ans)