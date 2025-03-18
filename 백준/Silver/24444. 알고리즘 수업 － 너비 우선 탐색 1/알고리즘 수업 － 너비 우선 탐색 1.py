from collections import deque
import sys

input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
order = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

cnt = 1
queue = deque([R])
order[R] = cnt

while queue:
    u = queue.popleft()
    for v in graph[u]:
        if order[v] == 0:
            cnt += 1
            order[v] = cnt
            queue.append(v)


print("\n".join(map(str, order[1:])))
