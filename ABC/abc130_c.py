w, h, x, y = map(int, input().split())
multi = 0
if w/2 == x and h/2 == y:
    multi = 1
print(w*h/2, multi)