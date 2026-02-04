T = int(input())
for tc in range(1, T+1) :
    # ==============================================
    # Normalize
    # ==============================================
    X, Y = map(int, input().split()) # X 이상 Y 이하
    lst = list(map(int, input().split()))
    tot = sum(lst)

    # ==============================================
    # Identify & Apply
    # 만족하면 바로 return을 하면 되겠다.
    #
    # ==============================================
    flag = 0
    def dfs(depth, curr_sum) :
        global flag
        # 시작도 전에
        if tot < X :
            return

        # 조건을 만족하는 경우 한번이라도 있다면 flag변경 : Yes
        if X <= curr_sum <= Y :
            flag = 1
            return

        if depth == 5 : # 4를 지나면 5개 선택완료인데 위의 조건을 거치지 않았기 때문에
            return

        dfs(depth+1, curr_sum + lst[depth]) # 선택
        dfs(depth+1, curr_sum) # 비선택


    # ==============================================
    # Report
    # ==============================================
    dfs(0, 0)
    if flag : print("YES")
    else : print("NO")