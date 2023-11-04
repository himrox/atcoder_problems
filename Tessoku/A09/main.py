H, W, N = map(int, input().split())
point_list = [list(map(int, input().split())) for _ in range(N)]
masu_list = []

for i in range(H+1):
    tmp = []
    for j in range(W+1):
        tmp.append(0)
    masu_list.append(tmp)

for point in point_list:
    A = point[0]
    B = point[1]
    C = point[2]
    D = point[3]
    masu_list[A-1][B-1] += 1
    masu_list[A-1][D] -= 1
    masu_list[C][B-1] -= 1
    masu_list[C][D] += 1

sum_masu_list = []

for i in range(H+1):
    sum = 0
    sum_list = []
    for j in range(W+1):
        sum += masu_list[i][j]
        sum_list.append(sum)
    sum_masu_list.append(sum_list)

for i in range(W+1):
    sum = 0
    for j in range(H+1):
        sum += sum_masu_list[j][i]
        sum_masu_list[j][i] = sum

for sum_masu in sum_masu_list:
    del sum_masu[-1]

del sum_masu_list[-1]

for ans in sum_masu_list:
    print(" ".join(map(str, ans)))
