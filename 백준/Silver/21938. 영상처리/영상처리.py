# 입력받고 전처리
N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]
for x in range(N) :
    row = list(map(int, input().split()))
    for y in range(M) :
        arr[x][y] = sum( row[3*y : 3*(y+1)] ) // 3 # 평균내기
T = int(input())

# 0과 255로 변환
for x in range(N) :
    for y in range(M) :
        if arr[x][y] >= T :
            arr[x][y] = 255
        else :
            arr[x][y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y) :
    stk = [(x, y)]
    while stk :
        x, y = stk.pop()
        # 스택에서 나왔으면 0처리
        arr[x][y] = 0
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx <= N-1 and 0 <= ny <= M-1) and arr[nx][ny] == 255 :
                stk.append((nx, ny))


ans = 0
for x in range(N) :
    for y in range(M) :
        if arr[x][y] == 255 :
            dfs(x, y)
            ans += 1

print(ans)
