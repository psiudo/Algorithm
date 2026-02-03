N, M = map(int, input().split())

ans = [0] * (M) # ans 배열
# 아직 아무 선택하지 않았으면 depth = 0 , depth = 1은 첫번째 선택, s_i 는 시작인덱스
def dfs(depth, s_i) :
    # 종료조건은 depth만 보면 된다.
    if depth == M : # depth는 M까지 ( M개의 노드를 지나치기에 )
        print(*ans)
        return # return 잊지 말기, 그래야 백트래킹 할 수 있음

    for num in range(s_i, N+1) : # num은 1 ~ N까지 / 즉, ans에 저장될 숫자후보
        ans[depth] = num
        dfs(depth+1, num+1) # num은 다음 dfs for문의 시작인덱스


dfs(0, 1)