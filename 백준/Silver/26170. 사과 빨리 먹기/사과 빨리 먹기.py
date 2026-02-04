# ==============================================
# Normalize
# ==============================================
grid = [ list(map(int, input().split())) for _ in range(5) ]
x, y = map(int, input().split())
# =================================================
# Identify & Apply
# 최단 거리가 아니라 최소 이동 거리 = dfs
# 더 짧은 dist가 나타나면 갱신하는 식으로 하자.
# =================================================
def inb(x, y) :
    if 0 <= x <= 4 and 0 <= y <= 4 : return True
    return False

best = 10e18
dv = [(0,1), (1,0), (-1,0), (0,-1)]
def dfs(x, y, cnt, dist) : # 각각 x, y, 먹은 갯수, 거리
    global best

    if grid[x][y] == 1 :
        cnt += 1

    if cnt == 3 :
        if best > dist :
            best = dist
        return # 리턴 잊지 말기

    for i in range(4) :
        nx, ny = x + dv[i][0], y + dv[i][1]
        # 안쪽이고 방문하지 않았으며 아니고 벽도 아니라면
        if inb(nx, ny) and not v[nx][ny] and grid[nx][ny] != -1 :
            v[nx][ny] = 1
            dfs(nx, ny, cnt, dist+1)
            v[nx][ny] = 0
# ==============================================
# Report
# ==============================================
v = [ [0]*5 for _ in range(5) ]
v[x][y] = 1 # 처음 위치

dfs(x, y, 0, 0)

if best != 10e18 :
    print(best)
else :
    print(-1)
