N = int(input())
each = [0]*(N+1) # 각 원소가 순열의 원소를 차례대로 저장
v = [0]*(N+1) # 모든 "순열"이기에 v배열 생성
def dfs(depth) : # depth는 선택의 단계, 레벨
    if depth == N+1 :
        print(*each[1:])
        return

    for num in range(1, N+1) :
        if not v[num] :
            each[depth] = num # each뒤에 인덱스 번호는 depth임이 자명
            v[num] = 1
            dfs(depth+1)
            v[num] = 0

dfs(1) # 이번엔 depth 1부터 시작
