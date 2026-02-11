import heapq

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for i in range(M) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, target = map(int, input().split())

def dijkstra(start, target) :
    dist = [1e9] * (N+1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq :
        cur_cost, cur_node = heapq.heappop(pq)
        
        if cur_cost != dist[cur_node] :
            continue
        if cur_node == target :
            return cur_cost
        
        for nxt_node, edge_cost in graph[cur_node] :
            new_cost = cur_cost + edge_cost
            if new_cost < dist[nxt_node] :
                dist[nxt_node] = new_cost
                heapq.heappush(pq, (new_cost, nxt_node))
    return dist[target]
print(dijkstra(start, target))