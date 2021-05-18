txt_input = [[1,2],[2,3],[3,1]]


from collections import deque   #リストの両端をいじる時に強いやつ

n = int(input())                #頂点の数
graph = [deque([]) for i in range(n+1)]
for i in range(n):
    u, k, * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
    print(v)