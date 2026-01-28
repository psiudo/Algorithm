n = int(input())
start, goal = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(m) :
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
##########################################
v = [0]*(n+1)
ans = -1
q = [(start, 0)] # 시작지점, 촌수
while q :
    node, cnt = q.pop()
    if node == goal :
        ans = cnt
        break
    for nxt in adj[node] :
        if not v[nxt] :
            q.append((nxt, cnt+1))
            v[nxt] = 1

print(ans)
