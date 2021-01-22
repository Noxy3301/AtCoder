n = int(input())
ans = (n//10)*100
if n%10 >= 7:
    ans += 100
else:
    ans += (n%10)*15
print(ans)