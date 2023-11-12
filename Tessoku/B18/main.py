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

n, s = map(int, input().split())
a_list = list(map(int, input().split()))
dp = []

for _ in range(n + 1):
    dp.append([0] * (s + 1))

dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(s + 1):
        if dp[i-1][j] == 1:
            dp[i][j] = 1
        elif j - a_list[i-1] >= 0:
            if dp[i-1][j-a_list[i-1]] == 1:
                dp[i][j] = 1

if dp[n][s] == 1:
    i = n
    j = s
    ans = []

    while i > 0:
        a = a_list[i-1]
        if j - a >= 0:
            if dp[i-1][j-a] == 1:
                ans.append(i)
                j = j - a
        i -= 1
    
    ans.sort()
    print(len(ans))
    print(" ".join(map(str, ans)))
else:
    print("-1")
