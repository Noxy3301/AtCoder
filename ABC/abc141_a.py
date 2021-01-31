s = input()
d = ["Sunny", "Cloudy", "Rainy"]
for i in range(3):
    if s == d[i]:
        if i == 2:
            print(d[0])
        else:
            print(d[i+1])