n = int(input())
next_in = 1
stk = []
ans = []
for _ in range(n) :
    x = int(input())

    """
    next_in은 stk[-1]의 예비후보
    현재 들어오는 숫자보다 next_in이 클 때까지는 넣는다.
    만약 그렇게 했을 때,
    stk의 값이 현재 입력이라면 스택에서 팝해준다.
    만약 그런데 next_in은 이미 큰데 이를 만족하지 못한다면
    그건 모두 NO  
    """
    while next_in <= x :
        stk.append(next_in)
        ans.append('+')
        next_in += 1

    if stk[-1] == x :
        stk.pop()
        ans.append('-')

    else :
        ans = ["NO"]
        break

for i in range(len(ans)) :
    print(ans[i], end='\n')
