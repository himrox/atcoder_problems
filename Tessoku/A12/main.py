N, K = map(int, input().split())
A_list = list(map(int, input().split()))
left = 1
right = 1000000000

while left < right:
    m = (left + right) // 2
    count = 0

    for A in A_list:
        count += m // A

    # print(m)
    # print(count)
    # print("---")

    if count >= K:
        right = m
    else:
        left = m + 1

    # break

print(left)
