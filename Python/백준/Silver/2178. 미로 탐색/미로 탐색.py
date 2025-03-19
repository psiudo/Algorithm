from collections import deque

N, M = map(int, input().split())
labyrinth = [list(map(int, list(input().strip()))) for _ in range(N)]
# 각 행마다 하나의 정수로 방문 여부를 비트마스크로 관리 (초기값: 0은 모두 미방문)
visited = [0] * N

def mark_visited(i, j):
    global visited
    visited[i] |= (1 << j)

def is_visited(i, j):
    return (visited[i] & (1 << j)) != 0

queue = deque()
queue.append((0, 0, 1))  # (x, y, 거리)
mark_visited(0, 0)

while queue:
    x, y, dist = queue.popleft()
    if x == N-1 and y == M-1:
        print(dist)
        break
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if not is_visited(nx, ny) and labyrinth[nx][ny] == 1:
                mark_visited(nx, ny)
                queue.append((nx, ny, dist + 1))
