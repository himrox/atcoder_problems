N = int(input())
left = 0
right = 100
x = 0
count = 0

while count < 100:
    mid = (left + right) / 2
    ans = mid ** 3 + mid

    if ans == N:
        x = mid
        break
    elif ans > N:
        right = mid
    else:
        left = mid

    x = mid
    count += 1

print(x)
