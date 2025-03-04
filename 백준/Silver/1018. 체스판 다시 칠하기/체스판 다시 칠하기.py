
N, M = map(int, input().split())

board = []
B_first = "BWBWBWBW"
W_first = "WBWBWBWB"
cnt_list = []
def pattern_B(i, j, cnt, line) :
    if line == 9 :
        return cnt

    for p in range(0, 8) :
        if board[i][j + p] == B_first[p]:
            continue
        else:
            cnt += 1
    return pattern_W(i + 1, j, cnt, line + 1)

def pattern_W(i, j, cnt, line) :
    if line == 9 :
        return cnt

    for p in range(0, 8) :
        if board[i][j + p] == W_first[p]:
            continue
        else:
            cnt += 1
    return pattern_B(i + 1, j, cnt, line + 1)


for i in range(N):
    board.append(input())

for i in range(0, N - 7):
    for j in range(0, M - 7):
        cnt_list.append(pattern_B(i, j, 0, 1))
        cnt_list.append(pattern_W(i, j, 0, 1))

print(min(cnt_list))