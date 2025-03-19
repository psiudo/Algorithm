from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

# 32비트씩 나누어 비트마스크 관리
visited = [0] * ((N * M // 32) + 1)

def set_visited(x, y):
    idx = x * M + y
    visited[idx // 32] |= (1 << (idx % 32))

def is_visited(x, y):
    idx = x * M + y
    return visited[idx // 32] & (1 << (idx % 32))

def bfs():
    queue = deque([(0, 0, 1)])
    set_visited(0, 0)

    while queue:
        x, y, dist = queue.popleft()
        if x == N - 1 and y == M - 1:
            print(dist)
            return
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == 1 and not is_visited(nx, ny):
                    set_visited(nx, ny)
                    queue.append((nx, ny, dist + 1))

bfs()