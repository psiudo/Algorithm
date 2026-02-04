# ==============================================
# Normalize
# ==============================================
N, K = map(int, input().split())
lst = list(map(int, input().split()))
# =================================================
# Identify & Apply
# =================================================
cnt = 0
v = [0]*N
def dfs(depth, curr) :
    global cnt
    if curr < 0 :
        return

    if depth == N :
        cnt += 1
        return

    for idx, item in enumerate(lst) :
        if curr + item - K  >= 0 and not v[idx]:
            v[idx] = 1
            dfs(depth+1, curr+item-K)
            v[idx] = 0

# ==============================================
# Report
# ==============================================
dfs(0, 0)
print(cnt)