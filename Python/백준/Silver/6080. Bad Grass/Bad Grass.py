import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 늘림

R, C = map(int, input().split())
elevation = [list(map(int, input().split())) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(r, c):
    visited[r][c] = True
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and elevation[nr][nc] > 0:
            dfs(nr, nc)

def count_islands():
    island_count = 0
    for r in range(R):
        for c in range(C):
            if elevation[r][c] > 0 and not visited[r][c]:
                dfs(r, c)
                island_count += 1
    return island_count

result = count_islands()
print(result)
