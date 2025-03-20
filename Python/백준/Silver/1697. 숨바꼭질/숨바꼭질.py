import sys
from collections import deque
input = sys.stdin.readline  # 혹시 몰라서 유지

N, K = map(int, input().split())

def bfs():
    queue = deque([N])  # (x, time) 튜플 안 쓰고 그냥 x만 저장
    visited[N] = 0  # elapse 시간 저장

    while queue:
        x = queue.popleft()
        time = visited[x]
        if x == K:
            return time  # 방문 시간 그대로 출력

        for dx in [1, -1, 2]:
            nx = x + dx if dx != 2 else x * 2
            if 0 <= nx < 100001 and visited[nx] == -1:  # visited를 -1로 초기화
                queue.append(nx)
                visited[nx] = time + 1  # 시간 바로 저장

visited = [-1] * 100001  # -1로 초기화하면 `False` 체크보다 빠름
print(bfs())
