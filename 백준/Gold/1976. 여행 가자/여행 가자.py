
"""
읽기+구상 : 12:00 / 코드 : 16:00 / 디버깅 : 10:00 / 실패횟수 : 5 / 제출횟수 : 2
"""

"""
인접 행렬이 주어졌다.
E (A B) C B C (B) D
dfs또는 bfs 통해서 할 수 있을까? 복잡할 것 같다.
출제의도는 경유지가 상관없으므로 유니온 파인드를 통해
같은 루트를 공유하는지 조사하는 것?
"""

N = int(input()) # 1 ~ 200
M = int(input()) # 1 ~ 1000
adj_mat = []
for i in range(1, N+1) :
    adj_mat.append(list(map(int, input().split())))
# print(adj_mat) [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
lst = list(map(int, input().split())) # [1, 2, 3]
# ==================================================
parent = [i for i in range(N+1)] # 0 1 2 3 4 ... N

def find(x) :
    while parent[x] != x :
        parent[x] = parent[parent[x]] # 경로 압축
        x = parent[x]
    return x

size = [1]*(N+1)
def union(a, b) :
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b :
        return

    if size[root_a] >= size[root_b] :
        parent[root_b] = root_a
        size[root_a] += size[root_b]
    elif size[root_a] <= size[root_b] :
        parent[root_a] = root_b
        size[root_b] += size[root_a]
    return

for i in range(N) :
    for j in range(N) :
        if adj_mat[i][j] != 0 : # 여기는 0인덱스
            union(i+1, j+1) # 여기는 1인덱스

# 마지막 경로 압축
ans = set()
for node in lst :
    ans.add(find(node))

if len(ans) == 1 :
    print("YES")
else :
    print("NO")