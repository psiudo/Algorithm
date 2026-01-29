import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mat = [[0] * (N+1)]
for i in range(N) :
    mat.append([0]+list(map(int, input().split()))) 


for row in range(1, N+1) :
    running_row = 0
    for col in range(1, N+1) :
        running_row += mat[row][col]
        if row == 1 :
            mat[row][col] = running_row
        else :
            mat[row][col] = running_row + mat[row-1][col]


for _ in range(M) :
    x1, y1, x2, y2 = map(int, input().split())
    print(mat[x2][y2] - mat[x2][y1-1] - mat[x1-1][y2] + mat[x1-1][y1-1])
