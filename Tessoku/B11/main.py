import bisect

N = int(input())
A_list = list(map(int, input().split()))
Q = int(input())
X_list = []

for _ in range(Q):
    X_list.append(int(input()))

# print(X_list)

A_list.sort()

for x in X_list:
    print(bisect.bisect_left(A_list, x))
    