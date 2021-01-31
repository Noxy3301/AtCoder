d = [list(input()) for i in range(2)]
nakami_sort = []
nakami_sort.append("".join(sorted(d[0])))
nakami_sort.append("".join(sorted(d[1], reverse=True)))
zentai_sort = sorted(nakami_sort)
if d[0] == d[1]:
    print("No")
elif nakami_sort == zentai_sort:
    print("Yes")
else:
    print("No")