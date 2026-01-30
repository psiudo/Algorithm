stk = list(map(str, input()))

# 대칭성 때문에 굳이 리버스 할 필요없이 결과는 동일
# 문자열 길이 3이상 뽑아놓아도 된다.
h = 10
curr = stk.pop()
# 마지막 순간 생각
while stk :
    if curr == stk[-1] :
        h += 5
    else :
        h += 10

    curr = stk.pop()

print(h)
