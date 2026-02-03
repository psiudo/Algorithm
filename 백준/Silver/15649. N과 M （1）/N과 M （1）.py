N, M = map(int, input().split())

path = [] # 상태공간트리의 선택된 원소를 선택된 순서대로 저장하는 리스트
def dfs(depth) : # 아직 아무 선택하지 않았으면 depth = 0 , depth = 1은 첫번째 선택
    if len(path) == M :
        print(*path)
        return

    for i in range(1, N+1) :
        if i not in path : # path에 중복된 수가 있으면 안되기에
            path.append(i) # 경로에 들어가고
            dfs(depth+1) # 다음 선택으로
            path.pop()

dfs(0)