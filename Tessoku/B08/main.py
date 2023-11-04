N = int(input())
point_list = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
zahyo_list = [list(map(int, input().split())) for _ in range(Q)]
heimen_list = []

for i in range(1501):
    tmp = []
    for j in range(1501):
        tmp.append(0)
    heimen_list.append(tmp)

for point in point_list:
    heimen_list[point[0]][point[1]] += 1

heimen_sum_list = []

for i in range(1501):
    sum = 0
    sum_list = []
    for j in range(1501):
        sum += heimen_list[i][j]
        sum_list.append(sum)
    heimen_sum_list.append(sum_list)

for i in range(1501):
    sum = 0
    for j in range(1501):
        sum += heimen_sum_list[j][i]
        heimen_sum_list[j][i] = sum

for zahyo in zahyo_list:
    a = zahyo[0]
    b = zahyo[1]
    c = zahyo[2]
    d = zahyo[3]

    ans = heimen_sum_list[c][d] + heimen_sum_list[a-1][b-1] - heimen_sum_list[a-1][d] - heimen_sum_list[c][b-1]
    print(ans)
