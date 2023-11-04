N = int(input())
point_list = [list(map(int, input().split())) for _ in range(N)]
masu_list = []

for i in range(1501):
    tmp = []
    for j in range(1501):
        tmp.append(0)
    masu_list.append(tmp)

for point in point_list:
    A = point[0]
    B = point[1]
    C = point[2]
    D = point[3]
    masu_list[A][B] += 1
    masu_list[C][D] += 1
    masu_list[A][D] -= 1
    masu_list[C][B] -= 1

# for i in range(10):
#     tmp = []
#     for j in range(10):
#         tmp.append(masu_list[i][j])
#     print(tmp)

sum_masu_list = []

for i in range(1501):
    sum = 0
    tmp = []
    for j in range(1501):
        sum += masu_list[i][j]
        tmp.append(sum)
    sum_masu_list.append(tmp)

# for i in range(10):
#     tmp = []
#     for j in range(10):
#         tmp.append(sum_masu_list[i][j])
#     print(tmp)

for i in range(1501):
    sum = 0
    for j in range(1501):
        sum += sum_masu_list[j][i]
        sum_masu_list[j][i] = sum

# for i in range(10):
#     tmp = []
#     for j in range(10):
#         tmp.append(sum_masu_list[i][j])
#     print(tmp)

ans = 0

for i in range(1501):
    for j in range(1501):
        if sum_masu_list[i][j] > 0:
            ans += 1

print(ans)
