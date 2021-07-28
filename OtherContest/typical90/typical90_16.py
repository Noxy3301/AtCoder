n = int(input())
coins = list(map(int, input().split()))
coins.sort()

a_count = n//coins[0]
b_count, c_count = 0, 0

while a_count*coins[0] + b_count*coins[1] + c_count*coins[2] != n:
    print("hoge")