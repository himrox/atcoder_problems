N = int(input())
A_list = list(map(int, input().split()))
D = int(input())
LR_list = [list(map(int, input().split())) for _ in range(D)]

left_max_list = []
max = 0

for A in A_list:
    if A > max:
        left_max_list.append(A)
        max = A
    else:
        left_max_list.append(max)

# print(left_max_list)

right_max_list = []
max = 0

for A in reversed(A_list):
    if A > max:
        right_max_list.insert(0, A)
        max = A
    else:
        right_max_list.insert(0, max)

# print(right_max_list)

for LR in LR_list:
    L = LR[0]
    R = LR[1]
    left_max = left_max_list[L-2]
    right_max = right_max_list[R]
    if left_max > right_max:
        print(left_max)
    else:
        print(right_max)
        