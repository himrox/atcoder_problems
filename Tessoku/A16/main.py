# 1行1列の入力
# 文字列を受け取る場合
# S = input()
# 整数を受け取る場合
# N = int(input())
# 小数を受け取る場合
# F = float(input())

# 1行複数列の入力
# 文字列を受け取る場合
# A, B = input().split()
# 整数を受け取る場合
# X, Y, Z = map(int, input().split())
# 小数を受け取る場合
# H, M, S = map(float, input().split())

# 1行の配列の入力
# 文字列を受け取る場合
# A = input().split()
# 整数列を受け取る場合
# A = list(map(int, input().split()))
# 小数列を受け取る場合
# A = list(map(float, input().split()))

# 複数行の配列の入力
# 複数行の文字列を受け取る場合
# A = [input().split() for _ in range(N)]
# 複数行の整数列を受け取る場合
# A = [list(map(int, input().split())) for _ in range(N)]
# 複数行の小数列を受け取る場合
# A = [list(map(float, input().split())) for _ in range(N)]

import bisect

n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

for _ in range(2):
    a_list.insert(0, 0)

for _ in range(3):
    b_list.insert(0, 0)

dp = []

for _ in range(n + 1):
    dp.append(0)

for i in range(n + 1):
    if i == 0 or i == 1:
        dp[i] = 0
    if i == 2:
        dp[i] = a_list[2]
    else:
        dp[i] = min(dp[i-1] + a_list[i], dp[i-2] + b_list[i])

print(dp[n])
