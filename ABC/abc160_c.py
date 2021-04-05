k,n = map(int, input().split())
d = tuple(map(int, input().split()))

#一番距離が遠いところを探して消す
distance = [d[i+1]-d[i] for i in range(n-1)]
distance.append(k-d[-1] + d[0])
print(k-max(distance))