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

for i in range(1, n):
    x = i
    y = n - x
    