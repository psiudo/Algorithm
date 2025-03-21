import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
matrix_map = [list(map(int, list(input().strip()))) for _ in range(N)]

visited = [[[False, False] for _ in range(M)] for _ in range(N)]

def crash_bfs():
    q = deque([(0, 0, 1, 0)])
    visited[0][0][0] = True
    
    while q:
        x, y, steps, crashed = q.popleft()
        if x == N - 1 and y == M - 1:
            return steps
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if matrix_map[nx][ny] == 0 and not visited[nx][ny][crashed]:
                    visited[nx][ny][crashed] = True
                    q.append((nx, ny, steps + 1, crashed))
                elif matrix_map[nx][ny] == 1 and crashed == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    q.append((nx, ny, steps + 1, 1))
    return -1

print(crash_bfs())
