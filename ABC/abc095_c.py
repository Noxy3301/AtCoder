A, B, C, X, Y = map(int, input().split())
C = C*2
ans = 0
if A+B <= C:
    ans = A*X + B*Y
else:
    hoge = min(X, Y)
    X -= hoge
    Y -= hoge
    ans += C*hoge
    if X == 0:
        if B <= C:
            ans += B*Y
        else:
            ans += C*Y
    else:
        if A <= C:
            ans += A*X
        else:
            ans += C*X
print(ans)