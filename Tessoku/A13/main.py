N, K = map(int, input().split())
A_list = list(map(int, input().split()))
R_list = []

for i in range(N - 1):
    if i == 0:
        R = 1
    else:
        R = R_list[i-1]

    left_num = A_list[i]

    while True:
        if R == N:
            R_list.append(R)
            break

        right_num = A_list[R]

        if right_num - left_num <= K:
            R += 1
        else:
            R_list.append(R)
            break

ans = 0

for i in range(len(R_list)):
    ans += R_list[i] - (i + 1)

print(ans)
