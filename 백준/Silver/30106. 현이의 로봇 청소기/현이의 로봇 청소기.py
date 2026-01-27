N, M, K = map(int, input().split())

"""
특정 지점에서 시작된 시작점이 순회하면서
연결 지으면서 flll component를 구축하기
"""
arr = []
for _ in range(N) :
    arr.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(r, c) :
    stk = [(r, c)]
    while stk :
        x, y = stk.pop()
        v[x][y] = 1
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= N-1 and 0 <= ny <= M-1 and not v[nx][ny] :
                if abs(arr[nx][ny] - arr[x][y]) <= K :
                    v[x][y] = 1
                    stk.append((nx, ny))

v = [[0]*M for _ in range(N)]
cnt = 0
for x in range(N) :
    for y in range(M) :
        if not v[x][y] :
            dfs(x, y)
            cnt += 1

print(cnt)
