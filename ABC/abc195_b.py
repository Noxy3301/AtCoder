import math
a,b,w = map(float, input().split())
tiisai = math.ceil(w*1000/b)
dekai = math.floor(w*1000/a)
if tiisai - dekai == 1:
    print("UNSATISFIABLE")
else:
    print(tiisai, dekai)