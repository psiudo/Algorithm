T = int(input())
for tc in range(1, T+1) :
    M, N = map(int, input().split())
    mat = []
    for _ in range(N) :
        mat.append(list(map(int, input().split())))

    best = float('-inf')
    ans = []
    for y in range(M) :
        temp = 1
        for x in range(N) :
            temp *= mat[x][y]

        if temp >= best :
            best = temp
            ans.append(y+1)

    print(max(ans))