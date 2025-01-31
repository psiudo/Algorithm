N, M = map(int, input().split())
Matrix = []

for i in range(N) :
    row = list(map(int, input().split()))
    Matrix.append(row)

Matrix_2 = []


for i in range(N) :
    row = list(map(int, input().split()))
    Matrix_2.append(row)

Matrix_sum = [[0] * M for _ in range(N)] 
for i in range(N) :
    for j in range(M) : 
        Matrix_sum[i][j] = Matrix[i][j] + Matrix_2[i][j] 

for row in Matrix_sum:
    print(*row)