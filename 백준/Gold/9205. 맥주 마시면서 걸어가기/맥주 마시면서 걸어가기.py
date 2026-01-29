from collections import deque
t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    sx, sy = map(int, input().split())
    p = []
    for _ in range(n) :
        temp_x, temp_y = map(int, input().split())
        p.append((temp_x, temp_y))
    gx, gy = map(int, input().split())
    p = [(sx, sy)] + p + [(gx, gy)]
    ####################################################
    """
    인접리스트를 구축하자. 
    단순히 2000이하라면 연결 아니라면 연결 x
    """
    adj = [[] for _ in range(n+2)]
    # 시작노드 인덱스 0 / 도착노드 인덱스 n+1
    for i, pos in enumerate(p) :
        for j in range(i+1, n+2) :
            diff_x = abs(pos[0] - p[j][0])
            diff_y = abs(pos[1] - p[j][1])
            if diff_x + diff_y <= 1000 :
                adj[i].append(j)
                adj[j].append(i)

    ###################################################
    v = [0]*(n+2)
    def bfs(node) :
        q = deque([node])
        v[node] = 1
        while q :
            node = q.popleft()

            if node == n+1 :
                return "happy"

            for nxt in adj[node] :
                if not v[nxt] :
                    v[nxt] = 1
                    q.append(nxt)
        return "sad"
    print(bfs(0))