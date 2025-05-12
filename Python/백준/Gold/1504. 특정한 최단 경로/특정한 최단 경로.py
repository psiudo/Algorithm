import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N, E = map(int, input().split())
graph = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(heap, (cost, next_node))

    return distance

dist_start = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path1 = dist_start[v1] + dist_v1[v2] + dist_v2[N]
path2 = dist_start[v2] + dist_v2[v1] + dist_v1[N]

result = min(path1, path2)

print(result if result < float('inf') else -1)
