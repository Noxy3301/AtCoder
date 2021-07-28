n = int(input())
if n%2 == 0:
    for i in range(2**n):
        binary = bin(i)[2:].zfill(n)
        flag = True
        ans = ""
        tmp = 0
        for i in range(len(binary)):
            if binary[i] == "0":
                tmp += 1
                ans += "("
            else:
                tmp -= 1
                ans += ")"
                if tmp < 0:
                    flag = False
        if flag  == True and tmp == 0:
            print(ans)