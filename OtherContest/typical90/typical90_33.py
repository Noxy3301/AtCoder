h,w = map(int, input().split())

h_kazu = h//2 + h%2
w_kazu = w//2 + w%2

if h == 1 or w == 1:
    print(h*w)
else:
    print(h_kazu*w_kazu)