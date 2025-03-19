import sys
from collections import deque

def dfs(cur) :
    for neighbor in graph[cur] :
        if neighbor in VisitedOrder :
            continue
        VisitedOrder.append(neighbor)
        dfs(neighbor)

def bfs(start) :
    queue = deque([start])
    while queue :
        cur = queue.popleft()
        for neighbor in graph[cur] :
            if neighbor in VisitedOrder :
                continue
            VisitedOrder.append(neighbor)
            queue.append(neighbor)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

VisitedOrder = []
VisitedOrder = [V]
dfs(V)
print(" ".join(map(str, VisitedOrder)))


VisitedOrder = []
VisitedOrder = [V]
bfs(V)
print(" ".join(map(str, VisitedOrder)))
