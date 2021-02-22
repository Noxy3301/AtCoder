def base(num, sinsuu):
    var = 0
    for i in range(len(str(num))):
        str_num = str(num)
        var += int(str_num[i])*sinsuu**((len(str_num)-i-1))
    return var




x = int(input())
m = int(input())

hidari = int(sorted(list(str(x)),reverse=True)[0])
migi = 10**18

while hidari <= migi:
    mid = (migi+hidari)//2
    if base(x,mid) < m:
        hidari = mid+1
    else:
        migi = mid-1


print(base(x,mid))
if base(x,mid) > m:
    x -= 1
    print(base(x,mid))
print(mid-int(sorted(list(str(x)),reverse=True)[0])+1)
