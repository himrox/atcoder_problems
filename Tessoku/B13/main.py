N, K = map(int, input().split())
A_list = list(map(int, input().split()))
sum_list = [0]
sum = 0

for A in A_list:
    sum += A
    sum_list.append(sum)

R_list = []

for i in range(len(A_list)):
    left = sum_list[i]

    if i == 0:
        R = 1
    else:
        R = R_list[i-1]
    
    while True:
        if R == N + 1:
            R_list.append(R)
            break

        if sum_list[R] - left <= K:
            R += 1
        else:
            R_list.append(R)
            break

ans = 0

for i in range(len(R_list)):
    ans += R_list[i] - (i + 1)

print(ans)