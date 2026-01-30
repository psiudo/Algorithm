N, M = map(int, input().split())
mat1 = []
for _ in range(N) :
    mat1.append(list(map(int, input().split())))
mat2 = []
M, K = map(int, input().split())
for _ in range(M) :
    mat2.append(list(map(int, input().split())))
###### mat2를 전치행렬로 하면 편하겠다. ########
mat2 = list(zip(*mat2))
# i는 결과행렬의 행을 결정
# j는 결과행렬의 열을 결정

result = [[]*K for _ in range(N)]
for i in range(N) :
    for t in range(K) :
        temp = 0
        for j in range(M) :
            temp += mat1[i][j]*mat2[t][j] # 각자 다른 행 움직임
        result[i].append(temp)

for i in range(N) :
    print(*result[i])
