import heapq

# 0 현재 / 1 ~ N - 2 중간분기 / N-1 도착지
N, M = map(int, input().split())
# 1은 보인다. 0은 보이지 않는다. 1이라면 갈 수 없다.
branches = list(map(int, input().split()))
branches[N-1] = 0 # 갈 수 있는 곳으로 바꾸기


adj_lst = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())

    # 노드, 간선 가지치기
    if (branches[a] == 1 or branches[b] == 1):
        continue

    adj_lst[a].append((t, b))
    adj_lst[b].append((t, a))

dist = [10 ** 18] * N  # 거리 배열
hq = [(0, 0)]
heapq.heapify(hq)
while hq:
    cost, node = heapq.heappop(hq)

    if dist[node] < cost:
        continue

    # 가지치기
    if node == N - 1:
        break

    for w, nxt in adj_lst[node]:
        if dist[nxt] > w + cost:  # 비용이 더 싸다면
            if branches[nxt] == 0:  # 0인 곳만
                # 일종의 방문 표시 / 갱신
                dist[nxt] = w + cost
                heapq.heappush(hq, (w + cost, nxt))


if dist[N - 1] != 10 ** 18:
    print(dist[N - 1])
else:
    print(-1)
