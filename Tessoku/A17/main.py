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
a_list.insert(0, 0)
b_list.insert(0, 0)
b_list.insert(0, 0)
dp = [0] * n

for i in range(n):
    if i == 0:
        dp[0] = 0
    elif i == 1:
        dp[1] = a_list[1]
    else:
        dp[i] = min(dp[i-1] + a_list[i], dp[i-2] + b_list[i])

place = n - 1
ans = []

while True:
    ans.append(place + 1)
    if place == 0:
        break

    if dp[place] - a_list[place] == dp[place-1]:
        place = place - 1
    else:
        place = place - 2

ans.reverse()
print(len(ans))
print(" ".join(map(str, ans)))
