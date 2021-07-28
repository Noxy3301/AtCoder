def base8to9_ins8(num, loop):
    for _ in range(loop):
        string = str(num)
        base_10 = 0
        for i in range(len(string)):
            base_10 += int(string[i])*8**(len(string)-i-1)
        
        base_8 = ""
        while base_10 >= 9:
            if base_10%9 == 8:
                base_8 += "5"
            else:
                base_8 += str(base_10%9)
            base_10 = base_10 // 9
        if base_10 == 8:
            base_8 += "5"
        else:
            base_8 += str(base_10)
        num = base_8[::-1]
    return num

n,k = map(int, input().split())
print(base8to9_ins8(n,k))