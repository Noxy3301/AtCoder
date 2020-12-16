n = int(input())
data = [input() for i in range(n)]
 
ac = 0
wa = 0
tle = 0
re = 0
 
for d in data:
  if d == "AC":
    ac += 1
  elif d == "WA":
    wa += 1
  elif d == "TLE":
    tle += 1
  elif d == "RE":
    re += 1
 
print("AC x " + str(ac))
print("WA x " + str(wa))
print("TLE x " + str(tle))
print("RE x " + str(re))