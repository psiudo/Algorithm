"""
읽기 + 구상 : 5:00 / 코드 : 6:00 / 디버깅 : 0:00 / 실패횟수 : 0
"""
N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(M) :
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

ans = [0]
v = [0]*N
def dfs(depth, curr) :
    if depth == 5 : # 5명 선택 완료
        ans[0] = 1
        return

    for nxt in adj[curr] :
        if not v[nxt] :
            v[nxt] = 1
            dfs(depth+1, nxt)
            v[nxt] = 0

# 시작 지점이 여러곳
for start in range(N) :
   if not ans[0] :
       dfs(0, start)
   else : break

print(ans[0])