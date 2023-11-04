N, X = map(int, input().split())
A_list = list(map(int, input().split()))
ans = 0
L = 0
R = N + 1

while True:
    m = (L + R) // 2
    
    if A_list[m] == X:
        ans = m + 1
        break
    elif X > A_list[m] :
        L = m + 1
    else:
        R = m - 1

print(ans)
