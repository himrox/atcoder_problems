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
h_list = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    if i == 0:
        dp[0] = 0
    elif i == 1:
        dp[1] = abs(h_list[1] - h_list[0])
    else:
        dp[i] = min(abs(h_list[i] - h_list[i-1]) + dp[i-1], abs(h_list[i] - h_list[i-2]) + dp[i-2])

p = n
ans = []

while True:
    ans.append(p)

    if p == 1:
        break
    elif dp[p-1] - dp[p-2] == abs(h_list[p-1] - h_list[p-2]):
        p = p - 1
    else:
        p = p - 2

ans.reverse()
print(len(ans))
print(" ".join(map(str, ans)))
