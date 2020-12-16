N = int(input())
lim = 10**9 + 7
if N == 1:
  print(0)
else:
  print((10**N - 2*9**N + 8**N) % lim)