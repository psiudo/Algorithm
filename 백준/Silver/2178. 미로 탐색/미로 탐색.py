from collections import deque
import sys

def min_steps_in_maze(N, M, maze):
    # 방향 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 1D 배열로 플래튼 변환
    visited = [False] * (N * M)
    
    # BFS 큐 초기화
    queue = deque([(0, 0, 1)])  # (x, y, 현재 이동 거리)
    visited[0] = True  # 시작점 방문 처리

    while queue:
        x, y, dist = queue.popleft()
        
        # 목표 지점 도착 시 종료
        if x == N-1 and y == M-1:
            return dist

        # 네 방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                idx = nx * M + ny  # 1D 인덱스 변환
                
                if maze[nx][ny] == 1 and not visited[idx]:  # 이동 가능 & 방문 안 했으면
                    visited[idx] = True  # 방문 처리
                    queue.append((nx, ny, dist + 1))

    return -1  # 도달 불가능 (문제 조건상 없지만 안전장치)

# 입력 처리
N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

# 결과 출력
print(min_steps_in_maze(N, M, maze))
