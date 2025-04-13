import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for neighbor, weight in graph[now]:
            cost = dist + weight
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(q, (cost, neighbor))

dijkstra(K)

# 최적화된 출력
print('\n'.join(
    'INF' if distance[i] == INF else str(distance[i])
    for i in range(1, V + 1)
))
