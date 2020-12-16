N,X,T = map(int, input().split())
amari = N % X
sho = N // X
if amari != 0:
  sho += 1
 
print(sho*T)