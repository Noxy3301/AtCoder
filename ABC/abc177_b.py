S = input()
T = input()
ev = []
for i in range(len(S) - len(T) + 1):
  commit = 0
  for j in range(len(T)):
    if S[i + j] == T[j]:
      commit += 1
  ev.append(commit)
 
ev.sort(reverse=True)
print(len(T) - ev[0])