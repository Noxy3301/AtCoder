y,m,d = input().split("/")
y,m,d = int(y), int(m), int(d)
if y <= 2018:
    print("Heisei")
elif m <= 3:
    print("Heisei")
elif m == 4 and d <= 30:
    print("Heisei")
else:
    print("TBD")