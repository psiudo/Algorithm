from collections import deque

# 입력 처리
N, C = map(int, input().split())

# 트리 구조 저장을 위한 딕셔너리 초기화
tree = {i: [] for i in range(1, N+1)}

# 입력된 연결 정보를 트리에 저장
for _ in range(C):
    E_i, B1_i, B2_i = map(int, input().split())
    tree[E_i].append(B1_i)
    tree[E_i].append(B2_i)

# BFS를 위한 큐 초기화
queue = deque([1])  # 농장에서 시작
distances = [-1] * (N + 1)
distances[1] = 1  # 농장에서 1번 파이프까지의 거리는 1

# BFS 수행
while queue:
    current_pipe = queue.popleft()
    
    # 현재 파이프와 연결된 다른 파이프에 대해 거리 계산
    for neighbor in tree[current_pipe]:
        if distances[neighbor] == -1:  # 아직 방문하지 않은 경우
            distances[neighbor] = distances[current_pipe] + 1
            queue.append(neighbor)

# 결과 출력
for i in range(1, N + 1):
    print(distances[i])
