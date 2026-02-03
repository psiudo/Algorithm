N = int(input())
tree = {}
adj = [[] for _ in range(N+1)]
for _ in range(N-1) :
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# print(adj)
# [[], [2, 3], [1, 4], [1, 5, 6], [2, 7, 8], [3, 9, 10], [3, 11, 12], [4], [4], [5], [5], [6], [6]]
##############################################################
parent_list = [0]*(N+1) # 인덱스가 자식이고 값이 부모
stk = [(0, 1)]
while stk :
    parent, child = stk.pop()
    parent_list[child] = parent # 확정

    for nxt in adj[child] : # 연결된 다른 노드 탐색
        if nxt == parent_list[child] :
            continue

        stk.append((child, nxt)) # 이제 child가 부모자리로
###############################################################
for i in range(2, N+1) :
    print(parent_list[i])

