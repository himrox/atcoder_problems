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



from itertools import product
import bisect

# A_list = [1, 2, 3, 4]
# rep = len(A_list)

# for pro in product((0, 1), repeat=rep):
#     sum = 0
#     idx = 0
#     for i in pro:
#         if i == 1:
#             sum += A_list[idx]
#         idx += 1
#     print(sum)

N, K =  map(int, input().split())
A_list = list(map(int, input().split()))

mid = len(A_list) // 2
B_list = A_list[:mid]
C_list = A_list[mid:]

def get_sum_list(li):
    sum_list = []
    for pro in product((0, 1), repeat=len(li)):
        sum = 0
        idx = 0
        for i in pro:
            if i == 1:
                sum += li[idx]
            idx += 1
        sum_list.append(sum)
    return sum_list

B_sum_list = get_sum_list(B_list)
C_sum_list = get_sum_list(C_list)

B_sum_list.sort()
C_sum_list.sort()

ans = "No"

for b in B_sum_list:
    find = K - b
    ind = bisect.bisect_left(C_sum_list, find)
    if ind < len(C_sum_list):
        if find == C_sum_list[ind]:
            ans = "Yes"

print(ans)
