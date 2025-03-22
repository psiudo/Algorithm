import sys
input = sys.stdin.readline
from collections import deque


def bfs_2layer_wall_break(grid):
    N, M = len(grid), len(grid[0])

    # 2개의 레이어: 아직 벽 안 부숨, 이미 부숨
    visited_no_break = [[False] * M for _ in range(N)]
    visited_break = [[False] * M for _ in range(N)]

    queue = deque()
    queue.append((0, 0, 0, 1))  # (x, y, w, dist) w=0이면 아직 벽 안 부숨
    visited_no_break[0][0] = True

    while queue:
        x, y, w, dist = queue.popleft()

        if x == N - 1 and y == M - 1:
            return dist

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == 0:
                    # 길(0) → w 상태 그대로
                    if w == 0 and not visited_no_break[nx][ny]:
                        visited_no_break[nx][ny] = True
                        queue.append((nx, ny, 0, dist + 1))
                    elif w == 1 and not visited_break[nx][ny]:
                        visited_break[nx][ny] = True
                        queue.append((nx, ny, 1, dist + 1))
                else:
                    # 벽(1)이고, 아직 벽 안 부쉈을 때만 가능
                    if w == 0 and not visited_break[nx][ny]:
                        visited_break[nx][ny] = True
                        queue.append((nx, ny, 1, dist + 1))

    return -1

N, M = map(int, input().split())
grid = [list(map(int, list(input().strip()))) for _ in range(N)]
print(bfs_2layer_wall_break(grid))
