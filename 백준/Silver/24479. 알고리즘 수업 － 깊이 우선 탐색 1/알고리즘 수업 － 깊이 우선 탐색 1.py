import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 늘려줍니다.

def dfs(v):
    global counter
    # 현재 정점을 방문 처리하며 방문 순서를 기록합니다.
    order[v] = counter
    # 인접 정점을 오름차순으로 방문합니다.
    for u in graph[v]:
        if order[u] == 0:
            counter += 1
            dfs(u)

# 입력 처리
input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
order = [0] * (N + 1)  # 각 정점의 방문 순서를 저장할 리스트 (0은 미방문)

# 무방향 간선 정보를 그래프에 저장합니다.
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 각 정점의 인접 리스트를 오름차순으로 정렬합니다.
for i in range(1, N + 1):
    graph[i].sort()

# DFS 수행: 시작 정점 R에서 시작하며 방문 순서 counter를 1부터 시작합니다.
counter = 1
dfs(R)

# 결과 출력: 정점 1부터 N까지 DFS 방문 순서를 출력합니다.
for i in range(1, N + 1):
    print(order[i])
