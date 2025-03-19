import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
Labyrinth = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

count = 1
queue = deque([(0, 0, count)])

while queue:
    x, y, count = queue.popleft()
    if x == N-1 and y == M-1 :
        print(count)
        break
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and Labyrinth[nx][ny] == 1:
            visited[nx][ny] = True
            queue.append((nx, ny, count+1))
    
