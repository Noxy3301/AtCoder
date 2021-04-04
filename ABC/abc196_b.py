x = input()
if x.count(".") > 0:
    dot = x.index(".")
    print(x[:dot])
else:
    print(x)