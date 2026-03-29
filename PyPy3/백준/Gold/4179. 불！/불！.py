from collections import deque
# ===============================================================================
N, M = map(int, input().split())
grid = [ list(input()) for _ in range(N) ]
sx, sy = next((x, y) for x in range(N) for y in range(M) if grid[x][y] == "J")
grid[sx][sy] = '.'
fires = []
for x in range(N) :
    for y in range(M) :
        if grid[x][y] != "F" : continue
        fires.append((x, y))

dv = [(0,1),(1,0),(-1,0),(0,-1)]
# ===============================================================================
def inb(p, q) :
    return 0 <= p <= N-1 and 0 <= q <= M-1
# --------------------------------------------------------------
def bfs(sx, sy, fires) :
    # 방문배열
    v = [[0]*M for _ in range(N)]
    v[sx][sy] = 1
    # 큐 생성
    fq = deque(fires)
    q = deque([(0, sx, sy)])
    while fq or q :

        for _ in range(len(q)) :
            elapsed, x, y = q.popleft()

            # 지훈이가 움직인 위치에 불이 덮쳤다면
            if grid[x][y] == "F" :
                continue

            for dx, dy in dv :
                nx, ny = x + dx, y + dy
                # 종료조건
                if not inb(nx, ny) : return elapsed + 1
                if v[nx][ny] : continue
                if grid[nx][ny] == "#" : continue
                if grid[nx][ny] == "F" : continue
                v[nx][ny] = 1
                q.append((elapsed + 1, nx, ny))

        for _ in range(len(fq)) :
            x, y = fq.popleft()
            for dx, dy in dv :
                nx, ny = x + dx, y + dy
                if not inb(nx, ny) : continue
                if grid[nx][ny] == "#" : continue
                if grid[nx][ny] == "F" : continue

                grid[nx][ny] = "F" # 불 번짐
                fq.append((nx, ny))

    return "IMPOSSIBLE"
# =============================================================================
print(bfs(sx, sy, fires))
