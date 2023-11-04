H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
zahyo_list = [list(map(int, input().split())) for _ in range(Q)]
two_d_sumlist = []

for i in range(H):
    sum = 0
    sum_list = []

    for j in range(W):
        sum += X[i][j]
        sum_list.append(sum)
    
    two_d_sumlist.append(sum_list)

for i in range(W):
    sum = 0
    
    for j in range(H):
        sum += two_d_sumlist[j][i]
        two_d_sumlist[j][i] = sum

tmp = []
for _ in range(W):
    tmp.append(0)

two_d_sumlist.insert(0, tmp)

for _ in two_d_sumlist:
    _.insert(0, 0)

for zahyo in zahyo_list:
    A = zahyo[0]
    B = zahyo[1]
    C = zahyo[2]
    D = zahyo[3]
    ans = two_d_sumlist[C][D] + two_d_sumlist[A-1][B-1] - two_d_sumlist[A-1][D] - two_d_sumlist[C][B-1]

    print(ans)
