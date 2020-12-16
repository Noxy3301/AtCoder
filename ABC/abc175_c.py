X,K,D = map(int, input().split())
X = abs(X)
if X - K*D > 0:
  print(X - K*D)
else:
  needCount = X//D
  limX = X - needCount * D
  remK = K - needCount
  minusX = limX - D
  if remK % 2 == 0:
    print(limX)
  else:
    print(abs(minusX))