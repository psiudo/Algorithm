"""
    M
   ___
 |  y
N|x
 |
"""
import sys
sys.setrecursionlimit(10000)
############## 입력받기 ##############
M, N, K = map(int, input().split())
arr = [[0]*M for _ in range(N)]
for _ in range(K) :
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2) :
        for y in range(y1, y2) :
            arr[x][y] = 1
####################################
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y) :
    global size

    arr[x][y] = 1 # 방문
    size += 1 # size 증가

    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        # 경계 안이고 안 막혀있다면
        if (0 <= nx <= N-1 and 0 <= ny <= M-1) and arr[nx][ny] != 1 :
            dfs(nx, ny)

#####################################
cnt = 0
size_lst = []
for row in range(N) :
    for col in range(M) :
        size = 0
        if arr[row][col] == 0  :
            dfs(row, col)
            cnt += 1
            size_lst.append(size)
#####################################
size_lst.sort()
print(cnt)
print(*size_lst)
